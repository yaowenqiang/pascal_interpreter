class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_value):
        if new_value < 0:
            raise ValueError("marks cannot be negative")
        self._marks = new_value

    @classmethod
    def class_name(cls):
        return cls.__name__
    
    @staticmethod
    def is_valid_title(title_text):
        """Checks where the string can be used as a blog title."""
        return title_text.istitle() and len(title_text) < 60

student = Student()
print(student.marks)
print(student.class_name())
student.marks = -10

