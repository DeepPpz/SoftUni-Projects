drink_type = input()
sugar = input()
drinks_count = int(input())
total_price = 0

if drink_type == "Espresso":
    if sugar == "Without":
        total_price = (drinks_count * 0.90) * 0.65
    elif sugar == "Normal":
        total_price = drinks_count * 1.00
    elif sugar == "Extra":
        total_price = drinks_count * 1.20

    if drinks_count >= 5:
        total_price *= 0.75

elif drink_type == "Cappuccino":
    if sugar == "Without":
        total_price = (drinks_count * 1.00) * 0.65
    elif sugar == "Normal":
        total_price = drinks_count * 1.20
    elif sugar == "Extra":
        total_price = drinks_count * 1.60

elif drink_type == "Tea":
    if sugar == "Without":
        total_price = (drinks_count * 0.50) * 0.65
    elif sugar == "Normal":
        total_price = drinks_count * 0.60
    elif sugar == "Extra":
        total_price = drinks_count * 0.70

if total_price > 15:
    total_price *= 0.80

print(f"You bought {drinks_count} cups of {drink_type} for {total_price:.2f} lv.")
