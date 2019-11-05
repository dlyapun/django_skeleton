# coding=utf-8
from django.conf import settings


def contex_core(request):
    return {'site_url': settings.SITE_URL,
            'site_name': settings.SITE_NAME,
            'support_email_address': settings.SUPPORT_EMAIL_ADDRESS,}
