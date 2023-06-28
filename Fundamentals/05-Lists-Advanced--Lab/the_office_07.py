list_happiness = list(map(int, input().split()))
factor = int(input())

list_happiness = [el * factor for el in list_happiness]
average_happiness = sum(list_happiness) / len(list_happiness)
happy_people = len(list(filter(lambda x: x > average_happiness, list_happiness)))

if happy_people * 2 >= len(list_happiness):
    print(f'Score: {happy_people}/{len(list_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_people}/{len(list_happiness)}. Employees are not happy!')
