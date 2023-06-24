def draw_stars(start, end, step):
    for row in range(start, end, step):
        stars = '* ' * row
        spaces = ' ' * (n - row)

        print(spaces, end='')
        print(stars)


n = int(input())

draw_stars(1, n + 1, 1)
draw_stars(n - 1, 0, - 1)
