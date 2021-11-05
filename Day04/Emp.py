from inheritance import Person


class A:
    pass


class B:
    pass


class Emp(Person, A, B):
    # more specification
    ontime = True

    def __init__(self, name, dateofbirth, id, email, nationality, income):
        super().__init__(name, dateofbirth)
        # self.name = name
        # self.dataofbirth = dateofbirth
        self.id = id
        self.email = email
        self._nationality = nationality
        # self.__income = income

    # override ---> 2 methods with the same name --> function signature
    # are placed in parent and child class
    # different in function body
    def speak(self):
        # super().speak()
        print(f"you can reach me at {self.email}")

    # def speak(self, msg):
    #     print(f'{self.name}, {msg}')
    # def myfun(self, x=None,y=None):
    #     if x.isnumeric() and y.isnumeric():
    #         return x+y
    #     elif x.isalpha() and y.isalpha():
    #         return f"{x} {y}"
    @classmethod  # represent Emp class
    def createperson(cls):
        # return Person.createperson()
        print(cls)

    @staticmethod
    def calage(year):
        return 2021 - abs(year)


# e = Emp("Ali", 1992, 10, "ali@iti.com", "Egypt",1000)
# # e.dataofbirth = 1995  # new property
# print(e.calage(e.dataofbirth))  # static method
# e.speak()
# # e.speak()
# # m = Emp.createperson()
# print("hi")
print(Emp.createperson())
