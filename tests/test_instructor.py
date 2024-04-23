# tests/test_instructor_class.py
from django.test import TestCase
from scheduling.classes.instructor_class import InstructorClass


class InstructorClassTest(TestCase):
    def setUp(self):
        self.instructor = InstructorClass("Instructor User", "456-789-0123")

    def test_get_user(self):
        self.assertEqual(self.instructor.get_user(), "Instructor User")

    def test_set_user(self):
        self.instructor.set_user("New Instructor User")
        self.assertEqual(self.instructor.get_user(), "New Instructor User")

    def test_get_contact_info(self):
        self.assertEqual(self.instructor.get_contact_info(), "456-789-0123")

    def test_set_contact_info(self):
        self.instructor.set_contact_info("321-098-7654")
        self.assertEqual(self.instructor.get_contact_info(), "321-098-7654")
