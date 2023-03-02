num_electrons = int(input())

n, shells = 0, []

while num_electrons > 0:
    n += 1
    max_electrons = 2 * n ** 2

    if max_electrons > num_electrons:
        shells.append(num_electrons)
        break
    else:
       shells.append(max_electrons)
       num_electrons -= max_electrons

print(shells)