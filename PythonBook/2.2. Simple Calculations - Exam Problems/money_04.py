bit_count = int(input())
yuan_count = float(input())
commission = float(input()) / 100

total_sum = bit_count * 1168 + yuan_count * 0.15 * 1.76
total_sum /= 1.95
total_sum -= total_sum * commission

print(f'{total_sum:.2f}')