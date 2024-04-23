# scheduling/classes/contact_info_class.py

class ContactInfoClass:
    def __init__(self, user_id, email, phone_number):
        self._user_id = user_id
        self._email = email
        self._phone_number = phone_number

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, value):
        self._phone_number = value
