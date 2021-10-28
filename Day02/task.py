def registeration():
    fname = input("plz enter firstname")
    lname = input("plz enter firstname")

while True:
    choice = input("plz write l for login , r for registeration ")
    choice = choice.strip()
    if choice.isalpha():
        if choice == "r":
            registeration()
            break
        elif choice == "l":
            print("login")
            break


