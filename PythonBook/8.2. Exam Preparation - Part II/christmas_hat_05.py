n = int(input())

width = 4 * n + 1
height = 2 * n

top_dots = (width - 3) // 2
print("." * top_dots + "/|\\" + "." * top_dots)
print("." * top_dots + "\\|/" + "." * top_dots)

for i in range(height):
    hyphens = "-" * i
    dots = "." * ((width - 3 - i * 2) // 2)
    print(dots + "*" + hyphens + "*" + hyphens + "*" + dots)

end_stars = "*" * width
print(end_stars)
print("*", end='')
print(".*" * ((width - 1) // 2))
print(end_stars)
