# deal with of file

# open file
myfile = open("itipackage/data.txt", "r")  #default r ---> reading
print(myfile)
print(type(myfile))

# do task , read, write, append
# data = myfile.read()  # read content of the file into a string
# print(type(data))
# print(data)
# data = myfile.readline()
# print(data)
# data = myfile.readline()
# print(data)
# data = myfile.readline()
# print(data)
# data = myfile.readline()
# print(data)
#
# #moving the pointer
# myfile.seek(10)
# data = myfile.readline()
# print(data)
#readlines
# data = myfile.readlines()  # read file into list
# print(data)
# print(type(data))

# data = myfile.read(25)
# print(data)
myfile = open("itipackage/data.txt", "r")  #default r ---> reading
for line in myfile:
    print(line)
# close file
myfile.close()
# data = myfile.read()
