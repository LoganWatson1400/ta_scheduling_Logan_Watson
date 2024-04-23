# tests/test_ta_class.py
from django.test import TestCase
from scheduling.classes.ta_class import TAClass


class TATest(TestCase):
    def setUp(self):
        self.ta = TAClass("TA User", "123-456-7890")

    def test_get_user(self):
        self.assertEqual(self.ta.get_user(), "TA User")

    def test_set_user(self):
        self.ta.set_user("New TA User")
        self.assertEqual(self.ta.get_user(), "New TA User")

    def test_get_contact_info(self):
        self.assertEqual(self.ta.get_contact_info(), "123-456-7890")

    def test_set_contact_info(self):
        self.ta.set_contact_info("987-654-3210")
        self.assertEqual(self.ta.get_contact_info(), "987-654-3210")
