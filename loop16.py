cnt = 0
money = 0
amount = 50
while True:
    money += amount
    amount += 10
    cnt += 1
    print(f"Month {cnt}: {money}")
    if money >= 1000:
        print("Goal reached in month", cnt)
        break