class Car:
    def __init__(self,name, model):
        self.name = name
        self.model =model





class Emp:
    def __init__(self, id, firstname, lastname, salary, byear, car):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.byear = byear
        self.car =car

    ### OVVERIDE for the special method __str__, that is called when
    # you trying to print object

    def __str__(self):
        return f"[{self.firstname}@{self.lastname}m,,,,,]"

    def __len__(self):
        #must return with number
        return 3
    def __call__(self, *args, **kwargs):
        print(f"object with fname ={self.firstname} called")
        return self.firstname

    # developer use this function in debug
    # def __repr__(self):
    #     return f"Emp({self.firstname},{self.lastname})"

    def __del__(self):
        print("this object is deleted")

    #operator overloading
    def __add__(self, other):
        return f"{self.firstname} {other}"


c = Car("mycar","BMW")
e = Emp(10,"noha","shehab",1000,1992,c.__dict__)
# __dict__

print(e.__dict__)
# e2 = Emp(15,"Ahmed","Mostafa",1000, 1992)
# print(e +e2)


