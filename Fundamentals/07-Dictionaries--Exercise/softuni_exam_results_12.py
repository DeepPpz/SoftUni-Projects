student = input().split("-")
exam_results = {}

while student[0] != "exam finished":
    username, language = student[0], student[1]

    if language == "banned":
        for (lang, user) in exam_results.items():
            for u in user:
                if u == username:
                    exam_results[lang][u] = 0
    else:
        points = int(student[2])
        if language not in exam_results:
            exam_results[language] = {"counter": 0}

        if username in exam_results[language] and exam_results[language][username] != 0:
            prev_points = exam_results[language][username]
            exam_results[language][username] = max(prev_points, points)
        else:
            exam_results[language][username] = points
        exam_results[language]["counter"] += 1

    student = input().split("-")

print(f"Results:")
for (lang, user) in exam_results.items():
    for (u, p) in user.items():
        if p != 0 and u != "counter":
            print(f"{u} | {p}")

print(f"Submissions:")
for lang in exam_results:
    print(f"{lang} - {exam_results[lang]['counter']}")
