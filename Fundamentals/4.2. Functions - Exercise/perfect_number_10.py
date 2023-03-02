def check_perfect_number(a):
    proper_divisors = []

    for n in range(1, a):
        if a % n == 0:
            proper_divisors.append(n)

    if sum(proper_divisors) == a:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(check_perfect_number(number))