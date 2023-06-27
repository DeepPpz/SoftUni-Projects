chrysanthemum_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = input()
holiday = input()

total_price = 0

sum_flowers = chrysanthemum_count + rose_count + tulip_count

if season == 'Spring':
    if holiday == 'Y':
        total_price = (chrysanthemum_count * 2.00 + rose_count * 4.10 + tulip_count * 2.50) * 1.15
        if tulip_count > 7:
            total_price -= total_price * 0.05
        if sum_flowers > 20:
            total_price -= total_price * 0.20
    elif holiday == 'N':
        total_price = chrysanthemum_count * 2.00 + rose_count * 4.10 + tulip_count * 2.50
        if tulip_count > 7:
            total_price -= total_price * 0.05
        if sum_flowers > 20:
            total_price -= total_price * 0.20

elif season == 'Summer':
    if holiday == 'Y':
        total_price = (chrysanthemum_count * 2.00 + rose_count * 4.10 + tulip_count * 2.50) * 1.15
        if sum_flowers > 20:
            total_price -= total_price * 0.20
    elif holiday == 'N':
        total_price = chrysanthemum_count * 2.00 + rose_count * 4.10 + tulip_count * 2.50
        if sum_flowers > 20:
            total_price -= total_price * 0.20

elif season == 'Autumn':
    if holiday == 'Y':
        total_price = (chrysanthemum_count * 3.75 + rose_count * 4.50 + tulip_count * 4.15) * 1.15
        if sum_flowers > 20:
            total_price -= total_price * 0.20
    elif holiday == 'N':
        total_price = chrysanthemum_count * 3.75 + rose_count * 4.50 + tulip_count * 4.15
        if sum_flowers > 20:
            total_price -= total_price * 0.20

elif season == 'Winter':
    if holiday == 'Y':
        total_price = (chrysanthemum_count * 3.75 + rose_count * 4.50 + tulip_count * 4.15) * 1.15
        if rose_count >= 10:
            total_price -= total_price * 0.10
        if sum_flowers > 20:
            total_price -= total_price * 0.20
    elif holiday == 'N':
        total_price = chrysanthemum_count * 3.75 + rose_count * 4.50 + tulip_count * 4.15
        if rose_count >= 10:
            total_price -= total_price * 0.10
        if sum_flowers > 20:
            total_price -= total_price * 0.20

total_price += 2.00

print(f'{total_price:.2f}')
