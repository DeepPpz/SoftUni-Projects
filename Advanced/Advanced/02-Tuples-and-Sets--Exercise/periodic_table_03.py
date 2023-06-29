n = int(input())
periodic_table = {item for _ in range(n) for item in input().split()}

print(*periodic_table, sep='\n')

# print(*{item for _ in range(int(input())) for item in input().split()}, sep='\n')
