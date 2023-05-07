exams_results = {}
student_results = {}
sorted_results = {}

while True:
    command = input().split(" -> ")

    if command[0] == "no more time":
        break

    username, contest, points = command[0], command[1], int(command[2])

    if contest not in exams_results:
        exams_results[contest] = {username: points}
    elif username not in exams_results[contest]:
        exams_results[contest][username] = points
    else:
        exams_results[contest][username] = max(exams_results[contest].get(username), points)

for contest in exams_results:
    exams_results[contest] = dict(sorted(exams_results[contest].items(), key=lambda x: (-x[1], x[0])))

for contest in exams_results:
    print(f"{contest}: {len(exams_results[contest])} participants")
    counter = 1
    for (username, points) in exams_results[contest].items():
        print(f"{counter}. {username} <::> {points}")
        counter += 1

        if username not in student_results:
            student_results[username] = points
        else:
            student_results[username] += points

student_results = dict(sorted(student_results.items(), key=lambda x: (-x[1], x[0])))

print("Individual standings:")
counter = 1
for (student, score) in student_results.items():
    print(f"{counter}. {student} -> {score}")
    counter += 1
