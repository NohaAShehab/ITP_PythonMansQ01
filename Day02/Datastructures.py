# # sequence ---> like an array
# # basic data sturcure --> 6
# # list, tuple , dictionary ---> set
# # depends on sequence --> each element assigned a number
# # index -->start from
#
# mylist = []  # empty
# l2 = ["python","Django", "flask"]
# mylist = ["Ahmed", "Meicheel", "Noursine", "Marwa", 55, 5.5, True, l2]
# print(mylist)
# print(type(mylist))
# # get count of items
# print(len(mylist))
# # index  ---> use index to get certain element
# print(mylist[5])
# # data structure, mutable, immutable ?
# # list is mutable datatype
# # mylist = ["Ahmed", "Meicheel", "Noursine", "Marwa", 55, 5.5, True, l2]
# # mylist[5]=100  # within the available index
# # print(mylist)
# # # mylist[8] ="Test"
# # # appending new item
# # mylist.append("test")
# # print(mylist)
# # # insert, within the list body
# # mylist.insert(5, "Mohamed")
# # print(mylist)
# # mylist.insert(100, "abc")
# # print(mylist)
# # print(len(mylist))
# # # mylist.insert(-1, "testt2")
# # mylist.insert(4,"ggg")
# # print(mylist)
# # mylist.insert(-len(mylist), "MoAli")
# # print(mylist)
# mylist = ["Ahmed", "Meicheel", "Noursine", "Marwa", 55, 5.5, True, l2]
# # item = mylist.pop()  #pop item
# print(mylist)
# # print(item)
# # item = mylist.pop(3)
# # print(mylist,item)
# # remove certain itme
# # mylist.remove("5.5")
# # print(mylist)
# l1 = ["Ahmed", "aya","aya", "abdulrahman"]
# l2 = ["amr", "anas", "mohamedelsayed","marwa"]
# # extend
# # l1.extend(l2)
# # print(l1)
# # # concatenation list with anohter
# # l3 = l1 + l2
# # print(l3)
#
# # repetition
# # team = ["mohamed", "Ahmed"]*4
# # print(team)
#
# # iteration ---> list itertable datastructure
# # for loops
#
# # for item in mylist:
# #     print(item)
#
# l4 = [4,5.55, 7,8,100]
# #min
# print(min(l4))
# #maxfor
# print(max(l4))
#
# # membership
# # check existance of certain item in list
# l2 = ["amr", "anas", "mohamedelsayed","marwa"]
# print("Anas" in l2)

name = "ITI"
print(name.lower())  # accept mail from user , loginname