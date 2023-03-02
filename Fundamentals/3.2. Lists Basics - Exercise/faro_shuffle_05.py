orig_deck = input().split()
shuffles = int(input())

deck = orig_deck
divider = int(len(orig_deck) / 2)

for _ in range(shuffles):
    new_deck = []
    first_half = deck[0:divider]
    second_half = deck[divider:]

    for i in range(divider):
        new_deck.append(first_half[i])
        new_deck.append(second_half[i])

    deck = new_deck

print(deck)