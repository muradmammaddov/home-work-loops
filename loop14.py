#attempts = 0 while'ın içerisinde yazıldığı üçün həmişə dəyər 0-lanır ona görədə program səhv işləyir.
password = "secret"
attempts = 0
while True:
    entered = input("Enter a password: ")
    if entered == password:
        print("Welcome")
        break
    attempts += 1
    if attempts == 3:
        print("Account locked")
        break