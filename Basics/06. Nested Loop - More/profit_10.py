one_count = int(input())
two_count = int(input())
five_count = int(input())
total_sum = int(input())

for x in range(0, one_count + 1):
    total_one = x * 1
    for y in range(0, two_count + 1):
        total_two = y * 2
        for z in range(0, five_count + 1):
            total_five = z * 5
            if total_one + total_two + total_five == total_sum:
                print(f'{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {total_sum} lv.')