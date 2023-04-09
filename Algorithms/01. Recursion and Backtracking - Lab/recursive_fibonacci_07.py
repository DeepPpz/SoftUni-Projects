def calculate_fibonnaci(num):
    if num <= 1:
        return 1
    return calculate_fibonnaci(num - 1) + calculate_fibonnaci(num - 2)

num = int(input())

print(calculate_fibonnaci(num))
