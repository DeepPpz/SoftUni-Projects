def tribonacci_numbers(num):
    tribonacci_list = [1]

    for i in range(num - 1):
        next_num = sum(tribonacci_list[-3:])
        tribonacci_list.append(next_num)
    print(*tribonacci_list, sep=' ')


n = int(input())

tribonacci_numbers(n)
