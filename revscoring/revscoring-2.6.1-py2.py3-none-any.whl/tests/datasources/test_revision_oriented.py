from revscoring.datasources.revision_oriented import revision

from .util import check_datasource


def test_revision():
    check_datasource(revision.id)
    check_datasource(revision.timestamp)
    check_datasource(revision.comment)
    check_datasource(revision.byte_len)
    check_datasource(revision.minor)
    check_datasource(revision.content_model)
    check_datasource(revision.text)
    assert hasattr(revision, "parent")
    assert hasattr(revision, "user")
    assert hasattr(revision, "page")
    assert hasattr(revision, "diff")

    # revision.parent
    check_datasource(revision.parent.id)
    assert hasattr(revision.parent, "user")
    check_datasource(revision.parent.user.id)
    check_datasource(revision.parent.user.text)
    assert not hasattr(revision.parent.user, "info")
    check_datasource(revision.parent.timestamp)
    check_datasource(revision.parent.comment)
    check_datasource(revision.parent.byte_len)
    check_datasource(revision.parent.minor)
    check_datasource(revision.parent.content_model)
    check_datasource(revision.parent.text)
    assert not hasattr(revision.parent, "page")
    assert not hasattr(revision.parent, "parent")
    assert not hasattr(revision.parent, "diff")

    # revision.page
    check_datasource(revision.page.id)
    assert hasattr(revision.page, "namespace")
    check_datasource(revision.page.namespace.id)
    check_datasource(revision.page.namespace.name)
    check_datasource(revision.page.title)
    assert hasattr(revision.page, "creation")
    check_datasource(revision.page.creation.id)
    assert hasattr(revision.page.creation, "user")
    check_datasource(revision.page.creation.timestamp)
    check_datasource(revision.page.creation.comment)
    check_datasource(revision.page.creation.byte_len)
    check_datasource(revision.page.creation.minor)
    check_datasource(revision.page.creation.content_model)
    assert not hasattr(revision.page.creation, "page")
    assert not hasattr(revision.page.creation, "text")
    assert not hasattr(revision.page.creation, "diff")
    assert hasattr(revision.page, "suggested")
    check_datasource(revision.page.suggested.properties)

    # revision.page.creation.user
    check_datasource(revision.page.creation.user.id)
    check_datasource(revision.page.creation.user.text)
    assert hasattr(revision.page.creation.user, "info")
    check_datasource(revision.page.creation.user.info.editcount)
    check_datasource(revision.page.creation.user.info.registration)
    check_datasource(revision.page.creation.user.info.groups)
    check_datasource(revision.page.creation.user.info.emailable)
    check_datasource(revision.page.creation.user.info.gender)

    # revision.user
    check_datasource(revision.user.id)
    check_datasource(revision.user.text)
    assert hasattr(revision.user, "info")
    check_datasource(revision.user.info.editcount)
    check_datasource(revision.user.info.registration)
    check_datasource(revision.user.info.groups)
    check_datasource(revision.user.info.emailable)
    check_datasource(revision.user.info.gender)
    assert hasattr(revision.user, "last_revision")
    check_datasource(revision.user.last_revision.id)
    assert hasattr(revision.user.last_revision, "page")
    check_datasource(revision.user.last_revision.page.id)
    assert hasattr(revision.user.last_revision.page, "namespace")
    check_datasource(revision.user.last_revision.page.namespace.id)
    check_datasource(revision.user.last_revision.page.namespace.name)
    check_datasource(revision.user.last_revision.page.title)
    assert not hasattr(revision.user.last_revision.page, "creation")
    check_datasource(revision.user.last_revision.timestamp)
    check_datasource(revision.user.last_revision.comment)
    check_datasource(revision.user.last_revision.byte_len)
    check_datasource(revision.user.last_revision.minor)
    check_datasource(revision.user.last_revision.content_model)
    assert not hasattr(revision.user.last_revision, "user")
    assert not hasattr(revision.user.last_revision, "parent")
    assert not hasattr(revision.user.last_revision, "text")
    assert not hasattr(revision.user.last_revision, "diff")
