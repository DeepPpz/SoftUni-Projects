n = int(input())
periodic_table = {item for _ in range(n) for item in input().split()}

print(*periodic_table, sep='\n')
