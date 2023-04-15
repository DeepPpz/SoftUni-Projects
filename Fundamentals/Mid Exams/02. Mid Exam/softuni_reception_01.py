emp_one = int(input())
emp_two = int(input())
emp_three = int(input())
stud_count = int(input())

total_efficiency = emp_one + emp_two + emp_three
hours = 0

while stud_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        stud_count -= total_efficiency

print(f'Time needed: {hours}h.')