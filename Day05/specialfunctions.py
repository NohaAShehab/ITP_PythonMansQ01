class Emp:

    def __init__(self, id, firstname, lastname, salary, byear):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.byear = byear

    ### OVVERIDE for the special method __str__, that is called when
    # you trying to print object

    # def __str__(self):
    #     return f"[{self.firstname}@{self.lastname}m,,,,,]"

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



e = Emp(10,"noha","shehab",1000,1992)
e2 = Emp(15,"Ahmed","Mostafa",1000, 1992)
print(e +e2)

#
# print(e())  # make object callable
# # print(Emp.__repr__(e))
# print(e.__repr__())
# del(e)
# print(len(e))
#
# # print(e)
# # l = [4,56,6]
# # print(len(l))
# # print(Emp.__str__(e))
# #
# # # t = (2,4,6,6)
# # # print(enumerate(t))
# # # print(t)
# # # info = {"name":'jhjkh', "age":''}
# # # print(info.keys())
# #
# # print("noha")  # call __str__ function in class Str
# # print("noha".__str__())
# # print(str.__str__("noha"))
