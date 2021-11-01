# syntax error
# exception
# logical error
# def abc:
#     pass

# print(name)  # exceptions

# def add(x, y):
#     print(x * y)
#
# add(55,6)
###############
# print("hii")
# print(name)  # Name error 000> object from Exception
# print("hello world")
# name = "Ahmed"
try:
    print(name)
except Exception as e:
    print(f"an exception here {e}")
    # pass
else:
    # executed if there is no problem
    print("All is well")
finally:
    # executed always
    print("I will be called whatever happened")

print("After handling exception")

