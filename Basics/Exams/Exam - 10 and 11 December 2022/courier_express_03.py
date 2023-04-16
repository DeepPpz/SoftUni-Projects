package_weight = float(input())
service_type = input()
distance = int(input())

total_price = 0
overprice = 0

if service_type == 'standard':
    if package_weight < 1:
        total_price = distance * 0.03
    elif 1 <= package_weight < 10:
        total_price = distance * 0.05
    elif 10 <= package_weight < 40:
        total_price = distance * 0.10
    elif 40 <= package_weight < 90:
        total_price = distance * 0.15
    elif 90 <= package_weight < 150:
        total_price = distance * 0.20

elif service_type == 'express':
    if package_weight < 1:
        overprice = 0.8 * 0.03
        overprice = overprice * package_weight * distance
        total_price = (distance * 0.03) + overprice
    elif 1 <= package_weight < 10:
        overprice = 0.4 * 0.05
        overprice = overprice * package_weight * distance
        total_price = (distance * 0.05) + overprice
    elif 10 <= package_weight < 40:
        overprice = 0.05 * 0.10
        overprice = overprice * package_weight * distance
        total_price = (distance * 0.10) + overprice
    elif 40 <= package_weight < 90:
        overprice = 0.02 * 0.15
        overprice = overprice * package_weight * distance
        total_price = (distance * 0.15) + overprice
    elif 90 <= package_weight < 150:
        overprice = 0.01 * 0.20
        overprice = overprice * package_weight * distance
        total_price = (distance * 0.20) + overprice

print(f'The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_price:.2f} lv.')
