# l = [3, 5, 7, 9]  # itertable using items
#
# for item in l:
#     print(item)
#
# # generate list of items --> start from 0 to 10
# # l = [0,1,2,3,4]
# # # range function
#
# l = range(6,2,-1)  # create iterator , create list of item
# # step by default =1
# print(l)
# myl = []
# for i in l:
#     myl.append(i)
# print(myl)

my = ["Ahmed", "Amira","Anas", "Abdulrahman"]
for item in my:
    if item == "Abdulrahman":
        continue
    print(item)
else:
    print("testing else block")
