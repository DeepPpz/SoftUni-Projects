from math import log


num = int(input())
base = input()

if base == "natural":
    print(f"{log(num):.2f}")
else:
    print(f"{log(num, int(base)):.2f}")
