budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_total = gpu_amount * 250
cpu_total = gpu_total * 0.35 * cpu_amount
ram_total = gpu_total * 0.1 * ram_amount

total_price = gpu_total + cpu_total + ram_total

if gpu_amount > cpu_amount:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')