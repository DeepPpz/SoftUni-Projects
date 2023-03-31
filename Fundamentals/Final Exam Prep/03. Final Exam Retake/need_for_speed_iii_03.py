n = int(input())
garage = {}
MAX_FUEL = 75

for _ in range(n):
    car, mileage, fuel = map(str, input().split("|"))
    garage[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    line = input().split(" : ")
    command = line[0]

    if command == "Stop":
        for car in garage:
            print(f"{car} -> Mileage: {garage[car]['mileage']} kms, Fuel in the tank: {garage[car]['fuel']} lt.")
        exit(0)

    if command == "Drive":
        car, distance, fuel = line[1], int(line[2]), int(line[3])

        if fuel > garage[car]["fuel"]:
            print("Not enough fuel to make that ride")
            continue

        garage[car]["mileage"] += distance
        garage[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if garage[car]["mileage"] >= 100000:
            del garage[car]
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        car, fuel = line[1], int(line[2])
        curr_fuel = garage[car]["fuel"]

        if curr_fuel + fuel >= MAX_FUEL:
            amount = MAX_FUEL - curr_fuel
        else:
            amount = fuel

        garage[car]["fuel"] = min(MAX_FUEL, (curr_fuel + fuel))
        print(f"{car} refueled with {amount} liters")

    elif command == "Revert":
        car, km = line[1], int(line[2])
        mileage = garage[car]["mileage"]

        if mileage - km < 10000:
            garage[car]["mileage"] = 10000
        else:
            garage[car]["mileage"] -= km
            print(f"{car} mileage decreased by {km} kilometers")
