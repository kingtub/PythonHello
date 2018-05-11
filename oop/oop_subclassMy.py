# Coding=UTF-8


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Init {}".format(name))

    def tell(self):
        print("Name:{} Age:{}".format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print("Salary:{}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print("Marks {}".format(self.marks))


t = Teacher('Mr Zhang', 40, 30000)
s = Student('Li', 28, 75)

members = [t, s]

for member in members:
    member.tell()
