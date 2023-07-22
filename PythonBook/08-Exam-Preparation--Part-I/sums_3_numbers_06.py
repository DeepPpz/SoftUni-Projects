a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    if a > b:
        print(f"{b} + {a} = {c}")
    else:
        print(f"{a} + {b} = {c}")

elif a + c == b:
    if a > c:
        print(f"{c} + {a} = {b}")
    else:
        print(f"{a} + {c} = {b}")

elif b + c == a:
    if b > c:
        print(f"{c} + {b} = {a}")
    else:
        print(f"{b} + {c} = {a}")

else:
    print("No")
