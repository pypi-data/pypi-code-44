from psu_base.services import auth_service
from django.conf import settings
from django.urls import reverse


def auth(request):
    auth_object = auth_service.get_auth_object()
    return {'auth': auth_object}


def util(request):
    model = {
        'home_url': '/'
    }

    if settings.URL_CONTEXT:
        model['home_url'] = f"/{settings.URL_CONTEXT}/"

    return model
