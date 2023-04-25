students = int(input())
avg_grade = 0
failed_stud = good_stud = great_stud = excell_stud = 0

for i in range(students):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        failed_stud += 1
    elif 3.00 <= grade <= 3.99:
        good_stud += 1
    elif 4.00 <= grade <= 4.99:
        great_stud += 1
    elif 5.00 <= grade <= 6.00:
        excell_stud += 1

    avg_grade += grade

avg_grade = avg_grade / students
failed_stud = failed_stud / students * 100
good_stud = good_stud / students * 100
great_stud = great_stud / students * 100
excell_stud = excell_stud / students * 100

print(f"Top students: {excell_stud:.2f}%")
print(f"Between 4.00 and 4.99: {great_stud:.2f}%")
print(f"Between 3.00 and 3.99: {good_stud:.2f}%")
print(f"Fail: {failed_stud:.2f}%")
print(f"Average: {avg_grade:.2f}")
