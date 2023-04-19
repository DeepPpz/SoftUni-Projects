is_end = False

for i in range(1, 4):
    if not is_end:
        for j in range(3, 0, -1):
            if i + j == 2:
                is_end = True
                break
            print("%d %d" % (i, j))
