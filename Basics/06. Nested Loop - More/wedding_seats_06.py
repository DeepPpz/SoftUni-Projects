last_sector = input()
row_count = int(input())
odd_seats = int(input())

last_sector = ord(last_sector)
even_seats = odd_seats + 2
total_seats = 0

for sector in range(65, last_sector + 1):
    for row in range(1, row_count + 1):
        if row % 2 == 0:  # even
            for seat in range(97, 97 + even_seats):
                total_seats += 1
                print(f'{chr(sector)}{row}{chr(seat)}')
        else:  # odd
            for seat in range(97, 97 + odd_seats):
                total_seats += 1
                print(f'{chr(sector)}{row}{chr(seat)}')

    row_count += 1

print(f'{total_seats}')