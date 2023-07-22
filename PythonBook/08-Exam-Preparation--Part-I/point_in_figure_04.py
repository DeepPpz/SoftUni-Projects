x = int(input())
y = int(input())

point_in = (2 <= x <= 12 and -3 <= y <= 1) or (4 <= x <= 10 and -5 <= y <= 3)

if point_in:
    print("in")
else:
    print("out")
