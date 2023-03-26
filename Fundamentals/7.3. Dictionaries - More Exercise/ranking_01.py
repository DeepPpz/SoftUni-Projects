contests = {}
end_results = {}
best_results = {}

while True:
    curr_contest = input().split(":")
    if curr_contest[0] == "end of contests":
        break
    else:
        contests[curr_contest[0]] = curr_contest[1]

curr_result = input().split("=>")

while curr_result[0] != "end of submissions":
    contest, password = curr_result[0], curr_result[1]
    username, points = curr_result[2], int(curr_result[3])

    if contest not in contests or password != contests[contest]:
        curr_result = input().split("=>")
        continue

    if contest not in end_results:
        end_results[contest] = {username: points}
    elif username not in end_results[contest]:
        end_results[contest][username] = points
        best_results[username] = 0
    else:
        prev_points = end_results[contest][username]
        end_results[contest][username] = max(prev_points, points)

    curr_result = input().split("=>")

for (lang, stud) in end_results.items():
    for s in stud:
        best_results[s] += sum(stud.values())

rank_dict = dict(sorted(best_results.items(), key=lambda x: -x[1]))

best_candidate = next(iter(rank_dict.items()))
print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")
print("Ranking:")

for i in end_results:
    end_results[i] = dict(sorted(end_results[i].items(), key=lambda x: x[0]))
print(end_results)


for (lang, stud) in end_results.items():
    print(f"{stud}")
    for (k, v) in stud.items():
        print(f"#  {lang} - {v}")
