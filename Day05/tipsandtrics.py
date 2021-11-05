# # f  = open("test.txt","w")
# f.write("kljjkl")


# with open("names.txt","w") as f:
#     f.write("hii")

# with open("test.txt") as f:
#     print(f)


# list comperhension
# generate list ---> 0,2,4,6,8
# l =[]
# for i in range(0,9,2):
#     l.append(i)
#
# print(l)

myl =[x*2 for x in range(0,10) if x%2==0]
print(myl)

