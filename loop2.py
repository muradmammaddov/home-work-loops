child = 0
adult = 0
for i in range(1,6):
    visitor = int(input("Age of visitor: "))
    if visitor > 18:
        adult += 1
    else:
        child += 1
print("Child tickets: ", child)
print("Adult tickets: ", adult)
