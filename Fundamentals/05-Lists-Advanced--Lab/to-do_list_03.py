notes = ['x'] * 10

while True:
    curr_task = input().split('-')

    if curr_task[0] == 'End':
        break

    idx = int(curr_task[0]) - 1
    task = curr_task[1]
    notes.insert(idx, task)
    notes.pop(idx + 1)

result = [el for el in notes if el != 'x']
print(result)
