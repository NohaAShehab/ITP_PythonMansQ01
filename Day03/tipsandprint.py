#
# m = n = 100
# print("test")
# # is operator check datatype as well as , value inside variable.
# print(m is n )
#
# x, y = 10, 10
# print(x is y)
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)
# print(l1 is l2)
# print("test")
#
# l = ["Mohamed", "Ahmed", "Mostafa", "Mina","test", "jjj"]
# # a, b, *c, d = l
# # print(a, b, c,d)
#
# for i in l:  #list ---> is itertable object
#     print(i)

# print(l[4])
# create index for list ---> itertable object
# enumeration
# m = enumerate(l)
# print(type(m))
# print(m)  #enumerate object
# # item --> index
# # l = ["Mohamed", "Ahmed", "Mostafa", "Mina","test", "jjj"]
# '''
# index 0 ---> Mohamed,
# index 1 ---> Ahmed
# '''
# for index, item in m:
#     print(f"item at {index} = {item}")

# myinfo = {"name":"iti", "country":"Egypt"}
# info = enumerate(myinfo)
#
# name = "Mohamed"
# for i, val in info:
#     print(f"{i}:{val}")
#     print(myinfo[val])

l1 = ["Ahmed", "omar", "Ali"]
l2 = ["boared", "Sleepy", "joy"]
el1 = enumerate(l1)
# for index, item in el1:
#     print(f"{index} :{item} mood is {l2[index]}")
# packing the 2 variables into one variable
# zip
# l1 = ["Ahmed", "omar", "Ali"]
# l2 = ["boared", "Sleepy", "joy"]
# l3 = [10, 20,30]
# for name,mood in zip(l1, zip(l2,l3)):  # return new zip object
#     print(f"{name} mood is {mood}")
#
# print(type(zip(l1,l2)))  # zip object can be iterated to get the each item in form of typle
#
# for i in zip(l1,l2):
#     print(f" {i} {type(i)}")
# for i in range(0, len(l1)):
#     print(f"{i} :{l1[i]} mood is {l2[i]}")

# all and any
# l = ["Ahmed", True, "", 10, {}]  #
# print(any(l))  # return true if at least one item of the sequece evaluate to true
# l = (3, 5, 6)
# print(all(l))  # retrun true if all the items within the iteratble evaluate to True
# x = 10
# y = "test"
# print(all([x,y]))

# info = {"name":"iti", "country":"Egypt", 0:False}
# print(all(info))