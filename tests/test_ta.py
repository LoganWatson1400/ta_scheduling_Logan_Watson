# ta_scheduling/tests/test_ta.py
from django.test import TestCase
from django.contrib.auth.models import User
from scheduling.models import TA


class TAModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        TA.objects.create(user=test_user, contact_info='Test contact info')

    def test_ta_contact_info(self):
        ta = TA.objects.get(id=1)
        expected_contact_info = f'{ta.contact_info}'
        self.assertEqual(expected_contact_info, 'Test contact info')

    def test_ta_string_representation(self):
        ta = TA.objects.get(id=1)
        self.assertEqual(str(ta), ta.user.username)
