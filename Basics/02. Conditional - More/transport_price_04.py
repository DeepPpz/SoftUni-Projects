n = int(input())
time = input()

if n >= 100:
    total_price = n * 0.06
elif n >= 20:
    total_price = n * 0.09

else:
    if time == 'day':
        total_price = n * 0.79 + 0.7
    elif time == 'night':
        total_price = n * 0.9 + 0.7

print(f'{total_price:.2f}')