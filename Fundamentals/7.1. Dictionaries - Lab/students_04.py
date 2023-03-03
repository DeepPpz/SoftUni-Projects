data = input()
courses = {}

while ":" in data:
    name, student_id, course = data.split(":")

    if course not in courses:
        courses[course] = {student_id: name}
    else:
        courses[course][student_id] = name

    data = input()

curr_course = data.replace("_", " ")
students = courses[curr_course]

for student_id, name in students.items():
    print(f"{name} - {student_id}")
