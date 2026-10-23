balance = 500
while True:
    amount = int(input("Amount: "))
    if amount == 0:
        print("Goodbye")
        break
    elif amount < 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance = balance - amount
        print(f"Balance: {balance}")