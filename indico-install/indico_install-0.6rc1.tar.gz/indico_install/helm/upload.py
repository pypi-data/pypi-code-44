import os
import tarfile
from pathlib import Path

import click
from google.cloud import storage

from indico_install.utils import options_wrapper, run_cmd, current_user, string_to_tag

UPLOAD_BUCKET = "indico-templates"


@click.command("upload")
@click.pass_context
@click.option(
    "-t",
    "--tag",
    required=True,
    multiple=True,
    help="Subdirectory(s) of {UPLOAD_BUCKET} to upload to",
)
@options_wrapper(check_services=True)
def upload(ctx, tag, *, deployment_root, services_yaml, **kwargs):
    """
    Upload the gzipped templates directory and services.yaml to indico-templates/<TAG> for each tag.
    For each <RENDER>, indico render for those values and publish the generated templates also to indico-templates/<TAG>.
    Will only overwrite

    Requires service account key to be base64-encoded and stored in the GOOGLE_SERVICE_ACCOUNT environment variable for authentication
    """
    deployment_root = Path(deployment_root)
    templates_dir = deployment_root / "templates"

    upload_user = current_user()
    assert upload_user, "Current user is not correctly authenticated with gcloud"

    if upload_user == "service_acct":
        try:
            run_cmd(
                "echo $GOOGLE_SERVICE_ACCOUNT | base64 -d > google.json", silent=True
            )
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path("google.json"))
            client = storage.Client()
            upload_bucket = client.get_bucket(UPLOAD_BUCKET)
        except Exception as e:
            click.secho(f"Unable to access bucket for uploads: {e}", fg="red")
            return

    if not templates_dir.is_dir() or not services_yaml.is_file():
        click.secho(f"Could not find {templates_dir} or {services_yaml}", fg="red")
        return

    with tarfile.open(deployment_root / "templates.tar.gz", "w:gz") as tar:
        click.secho(f"Tar-ing templates {templates_dir}")
        tar.add(templates_dir, arcname="")

    final_tags = [string_to_tag(t) for t in tag]

    for upload_file in [services_yaml, deployment_root / "templates.tar.gz"]:
        for upload_path in final_tags:
            if upload_user == "service_acct":
                upload_bucket.blob(
                    f"{upload_path}/{upload_file.name}"
                ).upload_from_filename(filename=str(upload_file))
            else:
                run_cmd(f"gsutil cp {upload_file} gs://{UPLOAD_BUCKET}/{upload_path}/")

    click.secho("Uploads complete! Tags:\n - " + "\n - ".join(final_tags), fg="green")
    return final_tags
