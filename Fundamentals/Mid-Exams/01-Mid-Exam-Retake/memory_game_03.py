def validate_indexes(a, b, x):
    if a != b and 0 <= a < x and 0 <= b < x:
        return True
    return False


cards = [el for el in input().split()]
indexes = input().split()
turns = 1

while indexes[0] != 'end':
    idx_one, idx_two = map(int, indexes)

    if not validate_indexes(idx_one, idx_two, len(cards)):
        mid = len(cards) // 2
        cards.insert(mid, ('-' + str(turns) + 'a'))
        cards.insert(mid, ('-' + str(turns) + 'a'))
        print("Invalid input! Adding additional elements to the board")
    elif cards[idx_one] == cards[idx_two]:
        element = cards[idx_two]
        print(f'Congrats! You have found matching elements - {element}!')
        cards.pop(idx_one)
        cards.remove(element)
    else:
        print('Try again!')

    if len(cards) == 0:
        print(f'You have won in {turns} turns!')
        exit()

    indexes = input().split()
    turns += 1

print('Sorry you lose :(')
print(*cards, sep=' ')
