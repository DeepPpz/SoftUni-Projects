team = input()
played_games = int(input())
total_points = 0
wins = 0
draws = 0
loses = 0

for i in range(played_games):
    curr_game = input().lower()

    if curr_game == "w":
        wins += 1
        total_points += 3
    elif curr_game == "d":
        draws += 1
        total_points += 1
    elif curr_game == "l":
        loses += 1

if played_games == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {(wins / played_games * 100):.2f}%")
