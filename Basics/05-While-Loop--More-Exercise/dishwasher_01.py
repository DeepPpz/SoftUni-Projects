detergent = int(input())

detergent *= 750
day = 1
plates = 0
pots = 0

dishes = input()

while dishes != 'End':
    dishes = int(dishes)

    if day % 3 == 0:
        detergent -= dishes * 15
        pots += dishes
    else:
        detergent -= dishes * 5
        plates += dishes

    if detergent < 0:
        break

    day += 1
    dishes = input()

if detergent >= 0:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
