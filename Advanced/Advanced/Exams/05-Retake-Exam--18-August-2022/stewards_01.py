from collections import deque

seats = [x for x in input().split(', ')]
taken_seats = []
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])
rotations = 0

while True:
    rotations += 1
    num_1 = first_sequence.popleft()
    num_2 = second_sequence.pop()
    character = chr(num_1 + num_2)
    first_combination = str(num_1) + character
    second_combination = str(num_2) + character

    if first_combination in seats:
        seats.remove(first_combination)
        taken_seats.append(first_combination)
    elif second_combination in seats:
        seats.remove(second_combination)
        taken_seats.append(second_combination)
    elif first_combination in taken_seats or second_combination in taken_seats:
        continue
    else:
        first_sequence.append(num_1)
        second_sequence.appendleft(num_2)

    if len(taken_seats) == 3 or rotations == 10:
        break

print('Seat matches:', ', '.join(taken_seats))
print('Rotations count:', rotations)
