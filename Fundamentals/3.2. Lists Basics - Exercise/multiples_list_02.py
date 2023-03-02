factor = int(input())
count = int(input())

multiples = [factor]

for i in range(1, count):
     multiples.append(multiples[i-1] + factor)

print(multiples)