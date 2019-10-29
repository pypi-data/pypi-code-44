from __future__ import unicode_literals

from waldur_core.core import WaldurExtension


class RancherExtension(WaldurExtension):

    class Settings:
        WALDUR_RANCHER = {
            'RANCHER_NODE_CLOUD_INIT_TEMPLATE': '#cloud-config\n'
                                                'packages: \n'
                                                '  - curl\n'
                                                'runcmd:\n'
                                                '  - curl -fsSL '
                                                'https://get.docker.com -o get-docker.sh; sh get-docker.sh\n'
                                                '  - [ sh, -c, "{command}" ]\n'
        }

    @staticmethod
    def django_app():
        return 'waldur_rancher'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in
