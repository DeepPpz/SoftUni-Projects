def calculate_power(number, power):
    total_power = number ** power
    if total_power % 1 == 0:
        return int(total_power)
    return total_power


a = float(input())
b = float(input())
print(calculate_power(a, b))
