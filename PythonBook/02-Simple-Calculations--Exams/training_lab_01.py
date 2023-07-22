l = float(input()) * 100
w = float(input()) * 100

seats = l // 120
seats *= (w - 100) // 70
seats -= 3

print(round(seats))