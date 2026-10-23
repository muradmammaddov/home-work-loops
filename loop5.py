while True:
    password = input("new password:")
    if len(password) < 8:
        print("Too short, try again")
    else:
        print("Password is accepted")
        break