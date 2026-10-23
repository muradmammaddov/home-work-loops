count = 0
for i in range(2, 101):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        count += 1
        print(i, end = " ")
print("\nTotal: ", count)
