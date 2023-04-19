n = int(input())
fact = 1

while True:
    fact *= n
    n -= 1

    if n <= 1:
        break

print(fact)
