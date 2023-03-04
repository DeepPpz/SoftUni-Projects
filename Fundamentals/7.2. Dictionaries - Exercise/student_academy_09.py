n = int(input())
academy = {}

for i in range(n):
    student = input()
    grade = float(input())

    if student not in academy:
        academy[student] = []
    academy[student].append(grade)

for (student, grades) in academy.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")
