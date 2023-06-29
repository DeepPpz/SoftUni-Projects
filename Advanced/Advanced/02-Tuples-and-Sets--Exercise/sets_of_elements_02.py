n, m = map(int, input().split())

n_set = set([int(input()) for _ in range(n)])
m_set = set([int(input()) for _ in range(m)])

common_ints = n_set.intersection(m_set)

print(*common_ints, sep='\n')
