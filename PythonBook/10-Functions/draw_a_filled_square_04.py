def print_header_footer(n):
    for i in range(0, (n * 2)):
        print("-", end="")
    print()

def print_middle_row(n):
    print("-", end="")
    for i in range(0, n - 1):
        print("\\/", end="")
    print("-")


size = int(input())
print_header_footer(size)
for i in range(0, size - 2):
    print_middle_row(size)
print_header_footer(size)
