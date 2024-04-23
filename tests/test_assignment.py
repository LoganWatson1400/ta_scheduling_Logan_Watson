# tests/test_assignment_class.py
from django.test import TestCase
from scheduling.classes.assignment_class import AssignmentClass


class AssignmentClassTest(TestCase):
    def setUp(self):
        self.assignment = AssignmentClass(1, 101)

    def test_get_assignment_id(self):
        self.assertEqual(self.assignment.get_assignment_id(), 1)

    def test_set_assignment_id(self):
        self.assignment.set_assignment_id(2)
        self.assertEqual(self.assignment.get_assignment_id(), 2)

    def test_get_course_id(self):
        self.assertEqual(self.assignment.get_course_id(), 101)

    def test_set_course_id(self):
        self.assignment.set_course_id(102)
        self.assertEqual(self.assignment.get_course_id(), 102)
