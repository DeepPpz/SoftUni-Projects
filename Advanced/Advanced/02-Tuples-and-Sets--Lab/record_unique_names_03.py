n = int(input())
names = set([input() for x in range(n)])

print(*names, sep='\n')
