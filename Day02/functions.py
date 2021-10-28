# global scope
# validate input name , contains no spaces, alpha , not empty
# while True:
#     name = input("plz enter your name")
#     if name.isalpha():  # check all the chars within str should  a-z
#         break
# print(name)
#
# while True:
#     lname = input("plz enter your name")
#     if lname.isalpha():
#         break
# print(lname)
#

# def abc(name):  # function parameter
#     print(f"hii {name}")
#     return name # retrun with var
# abc("ali")
# print(abc("anas"))
# validate string
# def validateStr(var):
#     # print(len(var))
#     var=var.strip() # remove spaces from begining and end from sti
#     # print(len(str))
#     if var.isalpha():
#     return
#
# name = input("plz enter your name ")
# print("welcome to day02 python")
#
#
# def sayhello(name):
#     print(f"Hi {name}")
#     return
#
#
# sayhello("Micheal")
# validate name --->
# python --->
# def validateInput(myinput):
#     myinput = myinput.strip()
#     if myinput.isalpha():
#         return myinput
#     else:
#         return False
#
# while True:
#     name = input("plz enter your name ")
#     name = validateInput(name)
#     if name:  # evaluate True
#         break

# # dealing with string
# name = "         "
# if name.isspace():
#     print("plz enter valid")

# function, can accept default parmater
# def sayHello(name, day="Thursday"):
#     print(f"Hello {name}, {day}")
#
# sayHello("amira","sat")
# sayHello(day="sat", name="amira")
# sayHello()

# # define function accept unknown number of parameters , zero or more
# def testfunc(*var):
#     # local variable
#     print(type(var))  # read input parameters into a tuple
#     print(var)
#     for i in var:
#         print(i)
# testfunc("Ahmed","Ali","yara","test")
# print("#############################")
# testfunc(10,True, 20 ,"amira")

### **KWargs
def myKWFunction (**kwargs):
    print(type(kwargs))
    print(kwargs)

myKWFunction(name="Noha", track= "os")
myKWFunction(id=100, salary=1000)
myKWFunction(absent= False)
myKWFunction()