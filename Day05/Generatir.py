# generator iterator

# l = [3,4,5,6,8]
# # for item in l:
# #     print(item)
# myl = iter(l)
# # generator ---> create iterators 1,3,4,5
# create numbers iterators  ---> next()
# within function scope
# range ---> in genetator
#
# def myfun2():
#     l = []
#     for i in range(0,100000000000000000):
#         l.append(i)
#     return l
#
# print(myfun2())
def myfun():
    for i in range(10,100):  # only one place
        # return i
        yield i   # return generator object
#
# mygen = myfun()
# for i in range(0,10):
#     print(next(mygen))
# x = 10000000000000000000000000
# # i = 0 , 1,2,3,4
# print(myfun()) # generator object ---> iterate
# x=myfun()
# print(next(x))
# print(next(x))
# print(next(myfun()))

# mygen= myfun()
# print(type(mygen))
# print(next(mygen)) # iterate object
# # # print(next(mygen))
# # # print(next(mygen))

# for i in mygen:
#     print(i)
# x = range(0,10)
# print(next(x))
# for i in range(0,10):
#     print(i)
