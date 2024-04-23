# tests/test_contact_info_class.py
from django.test import TestCase
from scheduling.classes.contact_info_class import ContactInfoClass


class ContactInfoClassTest(TestCase):
    def setUp(self):
        self.contact_info = ContactInfoClass(1, "test@example.com", "123-456-7890")

    def test_get_user_id(self):
        self.assertEqual(self.contact_info.get_user_id(), 1)

    def test_set_user_id(self):
        self.contact_info.set_user_id(2)
        self.assertEqual(self.contact_info.get_user_id(), 2)

    def test_get_email(self):
        self.assertEqual(self.contact_info.get_email(), "test@example.com")

    def test_set_email(self):
        self.contact_info.set_email("newemail@example.com")
        self.assertEqual(self.contact_info.get_email(), "newemail@example.com")

    def test_get_phone_number(self):
        self.assertEqual(self.contact_info.get_phone_number(), "123-456-7890")

    def test_set_phone_number(self):
        self.contact_info.set_phone_number("987-654-3210")
        self.assertEqual(self.contact_info.get_phone_number(), "987-654-3210")
