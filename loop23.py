total = 480
temp_total = total
count = 0
i = 1
while True:
    time = int(input(f"Customer {i} needs (min): "))
    if time == 0:
        break
    if time > temp_total:
        print("Sorry come back tomorrow")
        break
    else:
        temp_total = temp_total - time
        count = count + 1
        i = i + 1
print("Customers served: ", count)
print("Minutes left: ", temp_total)