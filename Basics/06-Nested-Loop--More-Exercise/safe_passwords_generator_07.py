a = int(input())
b = int(input())
max_pass = int(input())

A = 35
B = 64
max_flag = False

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')

        max_pass -= 1
        if max_pass == 0:
            max_flag = True
            break

        if A == 55:
            A = 35
        else:
            A += 1

        if B == 96:
            B = 64
        else:
            B += 1

    if max_flag:
        break
