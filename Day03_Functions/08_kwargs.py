"""
Question:
Create a function that accepts any number of keyword
arguments using **kwargs.

Example:
student(
    name="Samrat",
    age=21,
    course="Python",
    university="Calcutta University"
)

Print all the provided student information.
"""

def student(**kwargs):
    print("Student Name:",kwargs["name"])
    print("Student age:",kwargs["age"])
    print("Student course:",kwargs["course"])
    print("Student university:",kwargs["university"])


student(
    name="Samrat",
    age=21,
    course="Python",
    university="Calcutta University"
)