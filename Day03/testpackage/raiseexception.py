# raising exceptions

def dividenumber(x,y):
    if y == 0:
        raise Exception("Division by zero not accepted")
    print("this is the function")
    return x/y

print(dividenumber(10,0))

