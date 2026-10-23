garage = 20
while True:
    command = input("Command: ")
    if command == "stop":
        break
    else:
        if command == "in":
            if garage > 0:
                garage -= 1
                print("Free spaces: ", garage)
            else:
                print("Garage full")
        elif command == "out":
            if garage < 20:
                garage += 1
                print("Free spaces: ", garage)
            else:
                print("Garage is empty")
        else:
            print("Invalid command")
