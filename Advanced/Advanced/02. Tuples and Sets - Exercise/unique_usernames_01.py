n = int(input())
usernames = set([input() for x in range(n)])

print(*usernames, sep='\n')
