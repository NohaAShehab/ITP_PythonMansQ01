# tuples --> sequce of immutable python objects
# just a sequnce like lists

t1 =("python", "flask", "React", "Linux")
print(t1)
# print(type(t1))
# print(t1[0])
# # t1[0]= "Python"
# print(len(t1))
# new tuple
# t2=("shellscript", "ux-ui","js")
# # concatination
# t3 = t1 + t2
# print(t3)

# tuple -- repetition
# team = ("mohamed",)*4
# print(type(team))
# print(team)
# print(type(team))

# iteration
for item in t1:
    print(item)

# check item existance
# if "flask" in t1:
#     print("we will study flask")

# casting list into tuple and viceversa?
# l1 = ["a", "b", "c"]
# t= tuple(l1)
# print(t)
t = ("r","g","ff")
# print(list(t))
# print(type(t))
# myl=list(t) # new object with type list
# print(type(myl), type(t))
#
t = (5,6,7,0)
print(min(t))
print(max(t))
print(t)

for item in t:
    print(item)