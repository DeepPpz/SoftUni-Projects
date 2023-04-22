movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != "Finish":
    free_seats = int(input())
    filled_seats = 0

    for i in range(free_seats):
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        filled_seats += 1

    total_tickets += filled_seats
    fullness = filled_seats / free_seats * 100
    print(f"{movie} - {fullness:.2f}% full.")

    movie = input()

student_tickets = student_tickets / total_tickets * 100
standard_tickets = standard_tickets / total_tickets * 100
kid_tickets = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kid_tickets:.2f}% kids tickets.")
