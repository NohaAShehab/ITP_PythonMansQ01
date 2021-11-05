class Student:
    def __init__(self, name, c1=0, c2=0):
        self.name = name
        self.c1 = c1
        self.c2 = c2

    # instance method
    def speak(self):
        print(self)

    # classmethod ---> object factory
    @classmethod
    def genStudent(cls):
        return cls("std",0,0)

    @staticmethod
    def checkpassed(deg1, deg2):
        if deg1 + deg2 >= 120:
            return "passed"
        else:
            return "failed"


s = Student("Ali", 40, 70)

# call static
print(s.checkpassed(s.c1,s.c2))
print(Student.checkpassed(s.c1,s.c2))
# check if student passed or not ---> pass > 60%




