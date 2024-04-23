# tests/test_course_class.py
from django.test import TestCase
from scheduling.classes.course_class import CourseClass


class CourseTest(TestCase):
    def setUp(self):
        self.course = CourseClass("Introduction to Programming", "A basic course on programming.")

    def test_get_title(self):
        self.assertEqual(self.course.get_title(), "Introduction to Programming")

    def test_set_title(self):
        self.course.set_title("Advanced Programming")
        self.assertEqual(self.course.get_title(), "Advanced Programming")

    def test_get_description(self):
        self.assertEqual(self.course.get_description(), "A basic course on programming.")

    def test_set_description(self):
        self.course.set_description("An advanced course on programming.")
        self.assertEqual(self.course.get_description(), "An advanced course on programming.")
