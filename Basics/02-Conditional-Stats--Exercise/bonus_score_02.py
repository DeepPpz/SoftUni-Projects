start_points = int(input())
bonus = 0

if start_points <= 100:
    bonus = 5
elif start_points <= 1000:
    bonus = start_points * 0.2
elif start_points > 1000:
    bonus = start_points * 0.1

if start_points % 2 == 0:
    add_bonus = 1
elif start_points % 10 == 5:
    add_bonus = 2
else:
    add_bonus = 0

total_bonus = bonus + add_bonus
total_points = start_points + total_bonus

print(total_bonus)
print(total_points)
