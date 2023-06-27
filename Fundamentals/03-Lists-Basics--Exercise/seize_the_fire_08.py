fires = input().split('#')
water_avail = int(input())

effort, total_fire = 0, 0

print('Cells:')

for i in range(len(fires)):
    curr_fire = fires[i].split(' = ')
    fire_value = int(curr_fire[1])

    if (curr_fire[0] == 'High' and 81 <= fire_value <= 125) or \
            (curr_fire[0] == 'Medium' and 51 <= fire_value <= 80) or \
            (curr_fire[0] == 'Low' and 1 <= fire_value <= 50):
        if water_avail < fire_value:
            continue
        else:
            effort += 0.25 * fire_value
            total_fire += fire_value
            water_avail -= fire_value
            print(f' - {fire_value}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
