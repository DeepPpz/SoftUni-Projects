name = input()

grade = 1
total_marks = 0
failed = 0

while grade <= 12:
    mark = float(input())

    if mark < 4.00:
        failed += 1
        if failed > 1:
            break
        continue

    total_marks += mark
    grade += 1

total_marks = total_marks / 12

if failed > 1:
    print(f'{name} has been excluded at {grade} grade')
else:
    print(f'{name} graduated. Average grade: {total_marks:.2f}')