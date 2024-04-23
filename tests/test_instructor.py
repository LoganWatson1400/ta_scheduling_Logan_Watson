# ta_scheduling/tests/test_instructor.py
from django.test import TestCase
from django.contrib.auth.models import User
from scheduling.models import Instructor


class InstructorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='instructoruser', password='12345')
        Instructor.objects.create(user=test_user, contact_info='Instructor contact info')

    def test_instructor_contact_info(self):
        instructor = Instructor.objects.get(id=1)
        expected_contact_info = f'{instructor.contact_info}'
        self.assertEqual(expected_contact_info, 'Instructor contact info')

    def test_instructor_string_representation(self):
        instructor = Instructor.objects.get(id=1)
        self.assertEqual(str(instructor), instructor.user.username)