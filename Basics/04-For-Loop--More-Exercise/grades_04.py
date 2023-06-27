students_count = int(input())

top_stud = 0
between_four_five = 0
between_three_four = 0
fail_stud = 0
average_grade = 0

for grades in range(students_count):
    grade = float(input())
    average_grade += grade

    if 2.00 <= grade <= 2.99:
        fail_stud += 1
    elif 3.00 <= grade <= 3.99:
        between_three_four += 1
    elif 4.00 <= grade <= 4.99:
        between_four_five += 1
    elif 5.00 <= grade <= 6.00:
        top_stud += 1

average_grade = average_grade / students_count
top_stud = top_stud / students_count * 100
between_four_five = between_four_five / students_count * 100
between_three_four = between_three_four / students_count * 100
fail_stud = fail_stud / students_count * 100

print(f'Top students: {top_stud:.2f}%')
print(f'Between 4.00 and 4.99: {between_four_five:.2f}%')
print(f'Between 3.00 and 3.99: {between_three_four:.2f}%')
print(f'Fail: {fail_stud:.2f}%')
print(f'Average: {average_grade:.2f}')
