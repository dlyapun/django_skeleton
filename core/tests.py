from django.test import TestCase
from core.email_service import EmailService
from django.conf import settings


class EmailServiceTestCase(TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        pass

    def test_core_context(self):
        response = self.client.get('/core/')
        
        self.assertEqual(response.context['site_url'], settings.SITE_URL)
        self.assertEqual(response.context['site_name'], settings.SITE_NAME)
        self.assertEqual(response.status_code, 200)

    def test_send_email(self):
        from django.template.loader import get_template
        email_content = get_template('emails/core.html')
        test = EmailService.send_email({'foo': 'bar'}, email_content, 'Subject', ['test@test.com'])
