from django.test import TestCase
from scheduling.models import Course


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(title='Test Course', description='This is a test course.')

    def test_course_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.title}'
        self.assertEqual(expected_object_name, 'Test Course')

