capacity = int(input())
fans = int(input())

a_fans = 0
b_fans = 0
v_fans = 0
g_fans = 0
perc_fans = 0

for sort in range(fans):
    sector = input()

    if sector == 'A':
        a_fans += 1
    elif sector == 'B':
        b_fans += 1
    elif sector == 'V':
        v_fans += 1
    elif sector == 'G':
        g_fans += 1

a_fans = a_fans / fans * 100
b_fans = b_fans / fans * 100
v_fans = v_fans / fans * 100
g_fans = g_fans / fans * 100
perc_fans = fans / capacity * 100

print(f'{a_fans:.2f}%')
print(f'{b_fans:.2f}%')
print(f'{v_fans:.2f}%')
print(f'{g_fans:.2f}%')
print(f'{perc_fans:.2f}%')
