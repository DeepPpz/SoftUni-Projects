n = int(input()) #area
w = float(input()) #width of tile
l = float(input()) #length of tile
m = int(input()) #width of bench
o = int(input()) #length of bench

total_area = n * n
tile_area = w * l
bench_area = m * o

tiles_count = (total_area - bench_area) / tile_area
time_need = tiles_count * 0.2

print(f'{tiles_count:.2f}')
print(f'{time_need:.2f}')