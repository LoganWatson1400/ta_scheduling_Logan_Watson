# ta_scheduling/tests/test_course.py
from django.test import TestCase
from scheduling.models import Course


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(title='Test Course', description='This is a test course.')

    def test_course_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.title}'
        self.assertEqual(expected_object_name, 'Test Course')

    def test_course_description(self):
        course = Course.objects.get(id=1)
        expected_description = f'{course.description}'
        self.assertEqual(expected_description, 'This is a test course.')

    def test_course_string_representation(self):
        course = Course.objects.get(id=1)
        self.assertEqual(str(course), course.title)
