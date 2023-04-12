n = int(input())

cols = 2 * (n + 1) + 2 * n + 1

# top side
for i in range(n + 1):
    if i == 0:
        curr_underscores = cols - 2 * (n + 1)
        print("." * (n + 1) + "_" * curr_underscores + "." * (n + 1))
    else:
        curr_dots = n + 1 - i
        curr_underscores = cols - (2 * curr_dots) - 4
        print("." * curr_dots + "//" + "_" * curr_underscores + r"\\" + "." * curr_dots)

# middle side
curr_underscores = (cols - 9) // 2
print("//" + "_" * curr_underscores + "STOP!" + "_" * curr_underscores + r"\\")

# bottom side
for i in range(n):
    if i == 0:
        curr_underscores = cols - 4
        print(r"\\" + "_" * curr_underscores + "//")
    else:
        curr_dots = i
        curr_underscores = cols - (2 * curr_dots) - 4
        print("." * curr_dots + r"\\" + "_" * curr_underscores + "//" + "." * curr_dots)
