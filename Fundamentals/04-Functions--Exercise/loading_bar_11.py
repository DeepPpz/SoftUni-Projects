def create_loading_bar(x):
    if x == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        perc = ['%' for _ in range(x // 10)]
        dots = ['.' for _ in range((100 - x) // 10)]

        print(f'{x}%', end=' [')
        print(*perc, sep='', end='')
        print(*dots, sep='', end=']\n')
        print('Still loading...')


num = int(input())

create_loading_bar(num)
