juniors_part = int(input())
seniors_part = int(input())
track = input()

total_money = 0

if track == 'trail':
    total_money = juniors_part * 5.50 + seniors_part * 7.00
elif track == 'cross-country':
    if (juniors_part + seniors_part) >= 50:
        total_money = juniors_part * 8.00 * 0.75 + seniors_part * 9.50 * 0.75
    else:
        total_money = juniors_part * 8.00 + seniors_part * 9.50
elif track == 'downhill':
    total_money = juniors_part * 12.25 + seniors_part * 13.75
elif track == 'road':
    total_money = juniors_part * 20.00 + seniors_part * 21.50

total_money -= total_money * 0.05

print(f'{total_money:.2f}')
