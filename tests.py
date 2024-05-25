from django.test import TestCase
from django.test import Client
from core import models

class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.programmer = models.Programmer.objects.create(
            surname = 'Шышкин',
            name = "Алексей",
            patronymic = "Андреевич",
            birthday = '1994.10.24',
            salary = '50000',
            is_teamlead = False,
            grade = 'intern',
        )

        def test_list(self):
            pass

        def test_detail(self):
            pass

        def test_create(self):
            pass
