import math

height = int(input())
width = int(input())
not_painted = int(input()) / 100
total_walls = math.ceil((height * width * 4) * (1 - not_painted))
total_painted = 0

command = input()

while command != "Tired!":
    total_painted += int(command)

    if total_walls <= total_painted:
        break

    command = input()

diff = total_walls - total_painted

if diff > 0:
    print(f"{diff} quadratic m left.")
elif diff == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(diff)} l paint left!")
