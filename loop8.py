def_username = "admin"
def_password = 1234
count = 0
while True:
    username = input("Username: ")
    password = input("Password: ")
    if username == def_username and password == def_password:
        print("Welcome!")
    else:
        count += 1
        print("Wrong username or password.")
    if count == 3:
        print("Account locked.")
        break