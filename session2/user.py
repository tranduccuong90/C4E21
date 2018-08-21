import getpass
print("This is superuser gateway")
user = input("username: ")

if user != "c4e":
    print("not superuser")
else:
    password = getpass.getpass("password: ")
    if password != "codeforchange":
        print("incorrect password")
    else:
        print("welcome, c4e")
    

