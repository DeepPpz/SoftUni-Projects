contests = {}
end_results = {}

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
        pass
    elif username not in end_results:
        end_results[username] = {contest: points}
    elif contest not in end_results[username]:
        end_results[username][contest] = points
    else:
        prev_points = end_results[username][contest]
        end_results[username][contest] = max(prev_points, points)

    curr_result = input().split("=>")

best_results = {}
for (stud, contest) in end_results.items():
    best_results[stud] = sum(contest.values())
rank_dict = dict(sorted(best_results.items(), key=lambda x: -x[1]))

best_candidate = next(iter(rank_dict.items()))  # return the first key-pair value
print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")
print("Ranking:")

sorted_results = dict(sorted(end_results.items(), key=lambda x: x[0]))
for stud in sorted_results:
    print(f"{stud}")
    for (contest, points) in sorted(sorted_results[stud].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
