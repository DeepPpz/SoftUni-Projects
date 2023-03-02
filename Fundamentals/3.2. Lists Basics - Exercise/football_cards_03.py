cards = input().split()

a_team, b_team = [], []
termination = False

for i in range(1, 11 +1):
    a_team.append(str(i))
    b_team.append(str(i))

for i in range(len(cards)):
    curr_card = cards[i].split('-')

    if curr_card[0] == 'A':
        if curr_card[1] not in a_team:
            continue
        else:
            a_team.remove(curr_card[1])
    elif curr_card[0] == 'B':
        if curr_card[1] not in b_team:
            continue
        else:
            b_team.remove(curr_card[1])

    if len(a_team) < 7 or len(b_team) < 7:
        termination = True
        break

print(f'Team A - {len(a_team)}; Team B - {len(b_team)}')
if termination:
    print('Game was terminated')