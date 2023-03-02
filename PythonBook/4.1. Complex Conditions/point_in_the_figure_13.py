h = int(input())
x = int(input())
y = int(input())

l1_border = 0 <= x <= 3 * h and (y == 0 or y == h)
w1_border = 0 <= y <= h and (x == 0 or x == 3 * h)
l2_border = h <= x <= 2 * h and (y == h or y == 4 * h)
w2_border = h <= y <= 4 * h and (x == h or x == 2 * h)
exception = h < x < 2 * h and y == h
inside_one = 0 < x < 3 * h and 0 < y < h
inside_two = h < x < 2 * h and h < y < 4 * h

if l1_border or l2_border or w1_border or w2_border:
    if exception:
        print('inside')
    else:
        print('border')
elif inside_one or inside_two:
    print('inside')
else:
    print('outside')