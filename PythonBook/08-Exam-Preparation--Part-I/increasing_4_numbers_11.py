n = int(input())
m = int(input())
valid_comb = False

for a in range(n, m + 1):
    for b in range(n, m + 1):
        if b > a:
            for c in range(n, m + 1):
                if c > b:
                    for d in range(n, m + 1):
                        if d > c:
                            valid_comb = True
                            print(f"{a} {b} {c} {d}")

if not valid_comb:
    print("No")
