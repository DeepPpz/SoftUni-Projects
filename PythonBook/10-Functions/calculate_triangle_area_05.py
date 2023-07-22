def get_triangle_area(length, height):
    area = (length * height) / 2
    if area % 1 == 0:
        return int(area)
    return area


a = float(input())
h = float(input())
print(get_triangle_area(a, h))
