class Student:
    def __init__(self, name):
        self.name = name

    def issue(self, book):
        print(self.name, "issued", book)

s = Student("Abinaya")
s.issue("DBMS")