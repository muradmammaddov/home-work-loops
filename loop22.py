for i in range(1,6):
    if i == 4:
        continue
    print(f"Floor {i}: ", end = " ")
    for j in range(1, 5):
        print(100*i + j, end = " ")
    print()
