words = input().split()
result = ""

for w in words:
    result += w * len(w)

print(result)
