first = int(input())
second = int(input())
point = int(input())

x = min(first, second)
y = max(first, second)
to_x = abs(x - point)
to_y = abs(y - point)

if x <= point <= y:
    print("in")
else:
    print("out")
print(min(to_x, to_y))
