width = int(input())
length = int(input())

total_pieces = width * length

taken_pieces = input()

while taken_pieces != 'STOP':
    taken_pieces = int(taken_pieces)
    total_pieces -= taken_pieces

    if total_pieces <= 0:
        break

    taken_pieces = input()

if total_pieces >= 0:
    print(f'{total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
