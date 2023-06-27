max_fails = int(input())

score = 0
num_problems = 0
last_problem = ''
total_fails = 0
failed_flag = False

while True:
    problem = input()

    if problem == 'Enough':
        break

    grade = int(input())

    if grade <= 4:
        total_fails += 1
        if total_fails == max_fails:
            failed_flag = True
            break

    score += grade
    num_problems += 1
    last_problem = problem

score = score / num_problems

if failed_flag:
    print(f'You need a break, {total_fails} poor grades.')
else:
    print(f'Average score: {score:.2f}')
    print(f'Number of problems: {num_problems}')
    print(f'Last problem: {last_problem}')
