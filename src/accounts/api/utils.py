import datetime
from django.conf import settings
from django.utils import timezone

from rest_framework_jwt.settings import api_settings

expire_delta = api_settings.JWT_PAYLOAD_HANDLER

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }