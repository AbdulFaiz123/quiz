from collections import namedtuple

Internship = namedtuple("Intership", ["id","iname", "company", "i_year","status"])
Student = namedtuple("Student", ["usn", "name", "sem","placed"])
company = namedtuple("company,["name"])
Registration = namedtuple("Registration",["iid","usn","status"])