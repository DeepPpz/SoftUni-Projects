movie = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
current_tickets = 0
total_tickets = 0

while movie != 'Finish':
    free_seats = int(input())

    while free_seats > current_tickets:
        ticket = input()

        if ticket == 'End':
            break
        elif ticket == 'student':
            student_tickets += 1
            current_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
            current_tickets += 1
        elif ticket == 'kid':
            kid_tickets += 1
            current_tickets += 1

    print(f'{movie} - {current_tickets / free_seats * 100:.2f}% full.')
    total_tickets += current_tickets
    current_tickets = 0
    movie = input()

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
