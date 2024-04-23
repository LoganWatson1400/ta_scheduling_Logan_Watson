# scheduling/classes/instructor_class.py

class InstructorClass:
    def __init__(self, user, contact_info):
        self._user = user
        self._contact_info = contact_info

    def get_user(self):
        return self._user

    def set_user(self, value):
        self._user = value

    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, value):
        self._contact_info = value
