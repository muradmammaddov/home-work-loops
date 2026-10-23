def_pin = 2580
balance = 1000
attempt = 0
while True:
    pin = int(input('Enter pin number: '))
    attempt += 1
    if pin == def_pin:
        while True:
            print("1 - Check balance\n2 - Deposit\n3 - Withdraw\n4 - Exit")
            choose = int(input('Enter your choice: '))
            if choose == 1:
                print('Your balance is: ', balance)
            elif choose == 2:
                amount = int(input('Enter amount: '))
                balance += amount
                print('Your balance is: ', balance)
            elif choose == 3:
                amount = int(input('Enter amount: '))
                balance -= amount
                print('Your balance is: ', balance)
            elif choose == 4:
                print("Goodbye")
                break
        break
    else:
        if attempt == 3:
            print("Card blocked")
            break

