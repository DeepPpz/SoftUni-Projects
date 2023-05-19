n = int(input())
parking_lot = set()

for i in range(n):
    command = input().split(", ")

    if command[0] == "IN":
        parking_lot.add(command[1])
    elif command[0] == "OUT" and command[1] in parking_lot:
        parking_lot.remove(command[1])

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print("Parking Lot is Empty")
