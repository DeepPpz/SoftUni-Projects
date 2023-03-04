n = int(input())
parking = {}

for i in range(n):
    command = input().split()
    action, username = command[0], command[1]

    if action == "register":
        plate = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for (key, value) in parking.items():
    print(f"{key} => {value}")
