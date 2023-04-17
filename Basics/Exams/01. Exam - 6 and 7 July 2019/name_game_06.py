winner = ""
win_points = 0

while True:
    name = input()
    curr_points = 0

    if name == "Stop":
        break

    for letter in name:
        num = int(input())

        if num == ord(letter):
            curr_points += 10
        else:
            curr_points += 2

    if curr_points >= win_points:
        winner = name
        win_points = curr_points

print(f"The winner is {winner} with {win_points} points!")
