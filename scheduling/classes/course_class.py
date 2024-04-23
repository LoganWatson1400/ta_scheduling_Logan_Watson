# scheduling/classes/course_class.py

class CourseClass:
    def __init__(self, title, description):
        self._title = title
        self._description = description

    def get_title(self):
        return self._title

    def set_title(self, value):
        self._title = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value
