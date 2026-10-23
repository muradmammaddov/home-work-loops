while True:
    card = input("Card number: ")
    if len(card) != 16:
        print("Must be 16 digits")
    else:
        break
total = 0
reversed_card = card[::-1]
k = len(reversed_card)
m = 0
for i in range(k):
    if i % 2 == 0:
        m = int(reversed_card[i]) * 2
        if m > 9:
            m = m - 9
        total += m
    else:
        total += int(reversed_card[i])
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")



