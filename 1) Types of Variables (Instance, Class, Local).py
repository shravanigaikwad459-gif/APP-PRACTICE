class Student:
    college = "MIT ADT"      # Class Variable

    def __init__(self):
        self.name = "shravani"   # Instance Variable

    def display(self):
        income = 60000       # Local Variable
        print("Name:", self.name)
        print("College:", Student.college)
        print("Income:", income)

s = Student()
s.display()
