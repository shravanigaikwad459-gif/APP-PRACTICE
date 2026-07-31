class Student:
    def info(self):
        print("Student: shravaniiiii")

class Teacher:
    def info(self):
        print("Teacher: XYZ")

for x in (Student(), Teacher()):
    x.info()