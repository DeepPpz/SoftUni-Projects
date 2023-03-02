start_x = int(input())
start_y = int(input())
end_x = int(input())
end_y = int(input())

end_x = start_x + end_x
end_y = start_y + end_y
num_x, num_y = 0, 0
non_prime_x, non_prime_y = False, False

for x in range(start_x, end_x + 1):
    for y in range(start_y, end_y + 1):
        for i1 in range(2, x):
            if x % i1 == 0:
                non_prime_x = True
                break
            else:
                num_x = x

        for i2 in range(2, y):
            if y % i2 == 0:
                non_prime_y = True
                break
            else:
                num_y = y

        if not non_prime_x and not non_prime_y:
            print(f'{num_x}{num_y}')
        else:
            non_prime_x, non_prime_y = False, False