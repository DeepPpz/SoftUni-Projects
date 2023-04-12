n = int(input())

upper_pillar = "/" + ("^" * (n // 2)) + "\\"
mid_size = 2 * n - len(upper_pillar) * 2
bottom_pillar = "\\" + ("_" * (n // 2)) + "/"

print(upper_pillar + "_" * mid_size + upper_pillar)

for _ in range(n - 3):
    print("|" + (" " * (2 * n - 2)) + "|")

print("|" + (" " * (len(bottom_pillar) - 1)) + ("_" * mid_size) + (" " * (len(bottom_pillar) - 1)) + "|")
print(bottom_pillar + " " * mid_size + bottom_pillar)
