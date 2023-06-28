students = int(input())
lectures = int(input())
add_bonus = int(input())
max_bonus_points = 0
attendances = 0

for i in range(students):
    curr_attendances = int(input())
    curr_bonus = curr_attendances / lectures * (5 + add_bonus)
    max_bonus_points = max(max_bonus_points, curr_bonus)

    if curr_bonus == max_bonus_points:
        attendances = curr_attendances

print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {attendances} lectures.")
