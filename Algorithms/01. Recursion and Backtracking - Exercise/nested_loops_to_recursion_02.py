def execute_nested_loops(idx, recursion_list):
    if idx == n:
        print(*recursion_list, sep=' ')
        return
    for num in range(1, n + 1):
        recursion_list[idx] = num
        execute_nested_loops(idx + 1, recursion_list)


n = int(input())
recursion_list = [0] * n
execute_nested_loops(0, recursion_list)
