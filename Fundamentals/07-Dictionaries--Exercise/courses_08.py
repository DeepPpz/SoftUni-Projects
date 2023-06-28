total_courses = {}
data = input().split(" : ")

while data[0] != "end":
    course, student = data[0], data[1]

    if course not in total_courses:
        total_courses[course] = []
    total_courses[course].append(student)

    data = input().split(" : ")

for (key, value) in total_courses.items():
    print(f"{key}: {len(value)}")
    for st in value:
        print(f"-- {st}")
