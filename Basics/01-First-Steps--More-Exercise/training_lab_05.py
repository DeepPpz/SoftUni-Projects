w = float(input())
h = float(input())

h_places = (h - 1) // 0.7
w_places = w // 1.2
total_places = h_places * w_places - 3

print(total_places)
