n = int(input())

more_chairs, chairs_count = False, 0

for i in range(n):
    room = input().split()
    chairs, visitors = len(room[0]), int(room[1])
    diff = abs(chairs - visitors)

    if chairs < visitors:
        more_chairs = True
        print(f'{diff} more chairs needed in room {i + 1}')
    else:
        chairs_count += diff

if not more_chairs:
    print(f'Game On, {chairs_count} free chairs left')