total = 0.0
for i in range(1, 6):
    item = float(input(f"price of item {i}: "))
    total += item
avg = total / 5
print("Total: ", total)
print("Average: ", avg)