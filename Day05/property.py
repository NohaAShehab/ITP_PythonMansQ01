class Emp:

    def __init__(self, id, firstname, lastname, salary, byear):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.byear = byear


    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @fullname.setter
    def fullname(self,name):
        fname,lastname = name.split(" ")
        self.firstname = fname
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None


    #### restrict salary > 0 >>
    # calculated field
    @property
    def age(self):
        return 2021 - abs(self.byear)

    #
    @property
    def salary(self):
        if self.__sal != None:
            return self.__sal * .98
        else:
            return None

    @salary.setter
    def salary(self, sal): #None
        if isinstance(sal, int):
            self.__sal = abs(sal)  #None
            if self.__sal < 1000:
                self.__sal = 1000
            # if sal < 100:
            #     raise ValueError("sal should be > 1000")
            # self.__sal = 1000
        else:
            self.__sal= None

    @salary.deleter
    def salary(self):
        print("deleting salary")
        self.__sal =None
        self.salary = None  # call the setter function


try:
    e = Emp(1,"Ahmed","Ali",1000,1995)
except Exception as e:
    print(e)
else:
    # print(e.salary)  # property
    # print(e.age)
    # e.salary = -90
    # del e.salary
    print(e.fullname)
    del e.fullname
    print(e)


# print(abs("Ahmed")) # TypeError
# x = 10
# del (x) # del x
# print("jhiii")


e.fullname = "Noha Shehab"
# print(e.age)
# e.age= 20000

e.salary = 5000
print(e.salary)

del e

print("hiii")
print("test")

