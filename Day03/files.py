
try:
    f = open("myfile","w")
except:
    print("file not found")
else:
    f.close()

