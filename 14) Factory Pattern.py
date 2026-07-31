class Student:
    def show(self):
        print("Student: shravani")

class Factory:
    def create(self):
        return Student()

f = Factory()
obj = f.create()
obj.show()