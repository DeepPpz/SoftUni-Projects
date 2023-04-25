n = int(input())
m = int(input())
valid_combs = 0

for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left + 1, n + 1):
            for bottom in range(top + 1, n + 1):
                area = abs(right - left) * abs(bottom - top)

                if area >= m:
                    valid_combs += 1
                    print(f"({left}, {top}) ({right}, {bottom}) -> {area}")

if not valid_combs:
    print("No")
