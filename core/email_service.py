# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


class EmailService(object):

    ADMIN_EMAILS = []
    USER_EMAILS = []
    
    @staticmethod
    def send_email(context, email_content, subject, to_email):
        if settings.DEBUG_EMAIL:
            to_email = EmailService.USER_EMAILS

        context['domain'] = settings.SITE_URL

        html_content = email_content.render(context)
        msg = EmailMultiAlternatives(subject, html_content, settings.NO_REPLY_EMAIL_ADDRESS, to_email)
        msg.attach_alternative(html_content, 'text/html')
        return msg.send()
