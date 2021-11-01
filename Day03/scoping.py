# # scoping of variables..
# # global scope
# name = "iti from global scope"  # str
#
#
# # Wrapping for the variable
# def myfunction(info):  # local scope of the fucntion  (as parameter)
#     global name
#     print(name)
#     name = "Mohamed"  # lacal variable
#     msg = "Good morning "  # local variable in local scope
#     # name = input("plz enter your name")
#     # print(f"{msg} {name} {info}")
#
#     # inner function
#     def innerfunction(x):
#         id = 10
#         # print(msg,name,info)
#         print(id, x)  # x and id are local variables for the inner function
#
#     innerfunction("inner")
#     print("after execting inner function")
#
# myfunction("test")
# print(f"{name} from the global scope")
#
# def abc():
#     global name
#     print(f"calling from abc func {name}")
#     name = "Amira"
#
# abc()
# print(f"after calling abc function {name}")
iti = "Information Tech Institute"
def greetingfunc():
    # global iti
    # print(iti)
    # iti = "3>_ITI_<3"
    # print(iti)
    msg = "Hello Students"
    def innergreet():  # local function
        global iti
        msg = "Good morning MohamedHamed" # loccl var for inner greet
        print(f" inner function {msg} {iti}")
        iti = "I do love iti"
    innergreet()
    print(f" outer function {msg}")



greetingfunc()
print(iti)
