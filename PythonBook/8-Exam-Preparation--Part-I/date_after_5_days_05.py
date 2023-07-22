d = int(input()) + 5
m = int(input())

if m == 2:
    if d > 28:
        d -= 28
        m += 1
elif m in [4, 6, 9, 11]:
    if d > 30:
        d -= 30
        m += 1
else:
    if d > 31:
        d -= 31
        if m == 12:
            m = 1
        else:
            m += 1

print(f"{d}.{m:02d}")
