n = int(input())

print("+", end=' ')
for col in range(n-2):
    print("-", end=' ')
print("+")

for row in range(n-2):
    print("|", end=' ')
    for col in range(n-2):
        print("-", end=' ')
    print("|")

print("+", end=' ')
for col in range(n-2):
    print("-", end=' ')
print("+")
