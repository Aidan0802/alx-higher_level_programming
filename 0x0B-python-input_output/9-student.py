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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return student_dict
