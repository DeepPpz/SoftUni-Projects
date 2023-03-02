n = int(input())

presentation = input()
num_present = 0
total_grade = 0
avg_grade = 0

while presentation != 'Finish':
    for grades in range(n):
        grade = float(input())
        total_grade += grade
    total_grade /= n
    print(f'{presentation} - {total_grade:.2f}.')

    avg_grade += total_grade
    num_present += 1
    total_grade = 0
    presentation = input()

print(f"Student's final assessment is {avg_grade / num_present:.2f}.")