# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from core.email_service import EmailService


class AccountsEmailService(EmailService):

    @staticmethod
    def send_forgot_password(reset_data):
        to_email = [reset_data.user.email]
        email_content = get_template('emails/forgot_password_email.html')
        subject = 'Reset password request'
        context = {
            'reset_data': reset_data,
        }
        return AccountsEmailService.send_email(
            context, email_content, subject, to_email
        )

    @staticmethod
    def send_registration_email(user):
        to_email = [user.email]
        email_content = get_template('emails/registration_email.html')
        subject = 'Confirm Registration'
        context = {
            'user': user,
        }

        return AccountsEmailService.send_email(
            context, email_content, subject, to_email
        )
