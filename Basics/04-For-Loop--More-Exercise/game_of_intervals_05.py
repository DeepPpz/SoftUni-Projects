moves = int(input())

game_score = 0
til_ten = 0
til_twenty = 0
til_thirty = 0
til_forty = 0
til_fifty = 0
invalid_numbers = 0

for game in range(moves):
    current_move = int(input())

    if 0 <= current_move <= 9:
        til_ten += 1
        game_score += current_move * 0.2
    elif 10 <= current_move <= 19:
        til_twenty += 1
        game_score += current_move * 0.3
    elif 20 <= current_move <= 29:
        til_thirty += 1
        game_score += current_move * 0.4
    elif 30 <= current_move <= 39:
        til_forty += 1
        game_score += 50
    elif 40 <= current_move <= 50:
        til_fifty += 1
        game_score += 100
    else:
        invalid_numbers += 1
        game_score /= 2

til_ten = til_ten / moves * 100
til_twenty = til_twenty / moves * 100
til_thirty = til_thirty / moves * 100
til_forty = til_forty / moves * 100
til_fifty = til_fifty / moves * 100
invalid_numbers = invalid_numbers / moves * 100

print(f'{game_score:.2f}')
print(f'From 0 to 9: {til_ten:.2f}%')
print(f'From 10 to 19: {til_twenty:.2f}%')
print(f'From 20 to 29: {til_thirty:.2f}%')
print(f'From 30 to 39: {til_forty:.2f}%')
print(f'From 40 to 50: {til_fifty:.2f}%')
print(f'Invalid numbers: {invalid_numbers:.2f}%')
