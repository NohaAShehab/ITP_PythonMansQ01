'''
map real or logical instance into ---> OOP
'''


# class, object, method
# blueprint --> user created data structure  #template
class Employee:
    # class property, class variable
    nationality = "Egyptian"
    # pass
    # name, email, salary
    # define instance or object property
    # constructor --> specail function that can be used to create object
    # you need to define properties --
    # name, email, salary
    # custmoize object creation
    # instance level
    def __init__(self, name, email, salary):
        # instance property , instance variable
        # self ---> reference to the created objected
        # related to the self instance ---> instance varaibles
        print("object created")
        self.name = name
        self.email = email
        self.salary = salary

    # represent instance ---> intance method
    def speak(self):  # self --> instance from Employees
        print(f"Good morning I am {self.name}")


# object or instance
e = Employee("Ali", "ali@gmail.com", 10000)  # create object ---> instance # calling the constructor
e.speak()  # caller object from the class
# change intance variable valuesgmail
e2 = Employee("ola", "ola@gmail.com", 20000)

e.name = "Ahmed"
print("hi")
# # Employee.speak(e) # speak ---> employee object
print("test")
# e2.speak()

# accessing the class variable or class property using class name
# change value using Class Name, affect all class members
Employee.nationality = "Egy"
e3 = Employee("omar","sdffsd", 333)
print(e3.nationality)
e3.nationality = "Egypt"  # change class variable value in the caller intance
print("test")
