v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

fill_1 = p1 * h
fill_2 = p2 * h
total_fill = fill_1 + fill_2

if v >= total_fill:
    print(f'The pool is {total_fill / v * 100:.2f}% full. '
          f'Pipe 1: {fill_1 / total_fill * 100:.2f}%. Pipe 2: {fill_2 / total_fill * 100:.2f}%.')
else:
    print(f'For {h:.2f} hours the pool overflows with {total_fill - v:.2f} liters.')
