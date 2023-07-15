
class Student:

    def __init__(self, name, course, gpa, as_intern):
        self.name = name
        self.course = course
        self.gpa = gpa
        self.as_intern = as_intern

    def on_honour_roll(self):
        if self.gpa >= 7.5:
            return True
        else:
            return False