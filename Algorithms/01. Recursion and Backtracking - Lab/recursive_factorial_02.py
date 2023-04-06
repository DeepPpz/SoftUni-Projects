def find_factorial(n):
    if n == 1:
        return 1
    return n * find_factorial(n - 1)


n = int(input())
print(find_factorial(n))
