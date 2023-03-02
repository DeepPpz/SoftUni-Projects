width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

boxes = input()

while boxes != 'Done':
    boxes = int(boxes)
    free_space -= boxes

    if free_space <= 0:
        break

    boxes = input()

if free_space >= 0:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')