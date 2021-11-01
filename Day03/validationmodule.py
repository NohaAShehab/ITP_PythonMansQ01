## python file ---> organize for your
# user modules
# built-in modules
# validation funtion
x = 100
print("Good morning, Hope this day will be fine with you ")
def validateName(name):
    name =name.strip()
    if name.isalpha():
        if len(name) > 4:
            return name
        else:
            return False
    else:
        return False

def validateEmail(email):
    if len(email) >10:
        return email
    else:
        return False
