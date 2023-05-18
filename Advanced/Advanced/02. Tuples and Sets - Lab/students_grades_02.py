num_students = int(input())
students_data = {}

for i in range(num_students):
    curr_student = tuple(input().split())
    student, grade = curr_student

    if student not in students_data:
        students_data[student] = []
    students_data[student].append(float(grade))

for (student, grades) in students_data.items():
    avg = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(f'{x:.2f}' for x in grades)} (avg: {avg:.2f})")
