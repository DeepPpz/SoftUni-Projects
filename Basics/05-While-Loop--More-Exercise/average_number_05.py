n = int(input())

avg_sum = 0

for nums in range(n):
    number = int(input())
    avg_sum += number

print(f'{avg_sum / n:.2f}')
