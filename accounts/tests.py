# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User, ResetPasswordData

class AccountTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='first_user@test.com')
        self.user.set_password('password')
        self.user.save()

    def test_account_urls(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/forgot-password/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/accounts/change-password/token=1')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/accounts/confirm-registration/token=1')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/accounts/registration/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_user_login(self):
        user_data = {
            'email': 'first_user@test.com',
            'password': 'password',
        }
        response = self.client.post('/accounts/login/', user_data)
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        user_data = {
            'email': 'test@gmail.com',
            'password': 'password',
            'confirm_password': 'password'
        }
        response = self.client.post('/accounts/registration/', user_data)
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(email='test@gmail.com')

    def test_exist_user_registration(self):
        user_data = {
            'email': 'first_user@test.com',
            'password': 'password',
            'confirm_password': 'password'
        }
        response = self.client.post('/accounts/registration/', user_data)
        self.assertEqual(response.context['form'].errors['email'][0], 'User with this email already exist.')
        self.assertEqual(response.status_code, 200)

    def test_user_forgot_password(self):
        response = self.client.post('/accounts/forgot-password/', {'email': 'first_user@test.com'})
        self.assertEqual(response.status_code, 200)
        reset_token = ResetPasswordData.objects.first()
        self.assertEqual(reset_token.changed, False)
        self.assertEqual(reset_token.user, self.user)

        response = self.client.get('/accounts/change-password/token=' + reset_token.token)
        self.assertEqual(response.status_code, 200)

        password_data = {
            'new_password': 'new_password',
            'password_repeat': 'new_password'
        }

        response = self.client.post('/accounts/change-password/token=' + reset_token.token, password_data)
        self.assertEqual(response.status_code, 301)

        reset_token = ResetPasswordData.objects.first()
        self.assertEqual(reset_token.changed, True)

        response = self.client.post('/accounts/change-password/token=' + reset_token.token, password_data)
        self.assertEqual(response.context['expired'], True)
        self.assertEqual(response.status_code, 200)
