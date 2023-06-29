from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        queue.append(name)

while True:
    liters = input()

    try:
        liters = int(liters)
        if water_quantity >= liters:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    except ValueError:
        if "refill" in liters:
            liters = int(liters.split()[1])
            water_quantity += liters
        elif liters == "End":
            print(f"{water_quantity} liters left")
            exit(0)
