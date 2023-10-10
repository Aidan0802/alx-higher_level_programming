#!/usr/bin/python3
"""

This module contains a class Student

"""


class Student:
    """This is a class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of Student

        Args:
            parm1: Student first name
            parm2: Student last name
            parm3: Student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            parm1:
        """
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
