class Employee:
    nationality = "Egyption"  # class variables

    def __init__(self, name, email, salary, commission=0, netsalary=0, yearofbirth=1990):
        # define who can access these properties, like public
        self.name = name
        self.email = email
        self.salary = salary
        self._commission = commission  # protected
        self.__netsal = netsalary  # private
        self.yearofbirth = yearofbirth
        self.age = Employee.calage(yearofbirth)

    def speak(self, msg=""):  # instance method
        print(f"Good morning {self.name} {self.__netsal} {msg}")

    # class method ---> can be used to affect all the class instance
    # python decorator
    # @classmethod  # object form python decorator
    # object factory
    # def changeNationality(cls, nationality):  # represent caller class
    #     # call it using Classname
    #     print("Class method called ")
    #     cls.nationality =nationality
    #     # return new object from this class
    #     pass
    # factory method
    @classmethod
    def empFactory(cls):
        return cls("", "", 0)  # call __init__ method in the class

    # calculate age
    @staticmethod
    def calage(year):
        return 2021 - year


e2 = Employee("Noha", "nshehab@iti.gov.eg", 1000, 10, 10000, 1992)
e = Employee("Noha", "nshehab@iti.gov.eg", 1000)
e.name = "NohaShehab"
Employee.nationality = "Egypt"
print(e.name)
# e.speak()
# print(e.__netsal)
# print(e._commission)  #

# class method ---> object factory
m = Employee.empFactory()  # return object with type employee
print(type(m))

print(e.calage(e.yearofbirth))
print(Employee.calage(e2.yearofbirth))
