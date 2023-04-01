taxing_vehicles = input().split('>>')
total_taxes = 0

for i in range(len(taxing_vehicles)):
    curr_vehicle = taxing_vehicles[i].split()
    car_type = curr_vehicle[0]
    years = int(curr_vehicle[1])
    kilometers = int(curr_vehicle[2])

    if car_type == 'family':
        car_tax = 50
        car_tax -= 5 * years
        car_tax += 12 * (kilometers // 3000)
        total_taxes += car_tax
        print(f'A {car_type} car will pay {car_tax:.2f} euros in taxes.')

    elif car_type == 'heavyDuty':
        car_tax = 80
        car_tax -= 8 * years
        car_tax += 14 * (kilometers // 9000)
        total_taxes += car_tax
        print(f'A {car_type} car will pay {car_tax:.2f} euros in taxes.')

    elif car_type == 'sports':
        car_tax = 100
        car_tax -= 9 * years
        car_tax += 18 * (kilometers // 2000)
        total_taxes += car_tax
        print(f'A {car_type} car will pay {car_tax:.2f} euros in taxes.')

    else:
        print('Invalid car type.')

print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')