from django.test import TestCase
from django.db import IntegrityError
from .models import CallNotice

class CallNoticeModelTests(TestCase):
    def create_call_notice(self):
        title = 'Concurso Artístico'
        description = 'Lorem Ipsum'
        url = 'http://www.exemplo.com.br'
        call_notice = CallNotice.objects.create(title=title,
                                                description=description,
                                                url=url)
        return call_notice

    def test_creation(self):
        call_notice = self.create_call_notice()
        self.assertEqual(call_notice.title, 'Concurso Artístico')
        self.assertEqual(call_notice.description, 'Lorem Ipsum')
        self.assertEqual(call_notice.url, 'http://www.exemplo.com.br')

    def test_url_uniqueness(self):
        self.create_call_notice()

        with self.assertRaises(IntegrityError):
            self.create_call_notice()
