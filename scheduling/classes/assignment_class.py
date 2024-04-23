# scheduling/classes/assignment_class.py

class AssignmentClass:
    def __init__(self, assignment_id, course_id):
        self._assignment_id = assignment_id
        self._course_id = course_id

    def get_assignment_id(self):
        return self._assignment_id

    def set_assignment_id(self, value):
        self._assignment_id = value

    def get_course_id(self):
        return self._course_id

    def set_course_id(self, value):
        self._course_id = value
