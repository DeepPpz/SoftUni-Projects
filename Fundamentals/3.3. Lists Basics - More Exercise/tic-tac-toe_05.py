winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
    [0, 4, 8], [2, 4, 6]  # diagonal
]

row_one = input().split()
row_two = input().split()
row_three = input().split()

orig_input = row_one
orig_input.extend(row_two + row_three)
first_player, second_player = [], []

for i in range(len(orig_input)):
    if orig_input[i] == '1':
        first_player.append(i)
    elif orig_input[i] == '2':
        second_player.append(i)

if first_player in winning_combinations:
    print('First player won')
elif second_player in winning_combinations:
    print('Second player won')
else:
    print('Draw!')