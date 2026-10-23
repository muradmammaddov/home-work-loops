hottest = 0
cnt = 0
for i in range(1, 8):
    day = int(input(f"Day {i}: "))
    if day > hottest:
        hottest = day
    if day > 30:
        cnt += 1
print("Hot days: ", cnt)
print("Hottest day: ", hottest)
