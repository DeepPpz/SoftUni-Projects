cargo_count = int(input())

total_weight = 0
total_price = 0
average_price = 0
bus = 0
truck = 0
train = 0

for cargo in range(cargo_count):
    cargo_weight = int(input())
    total_weight += cargo_weight
    if cargo_weight < 4:
        bus += cargo_weight
        total_price += cargo_weight * 200
    elif cargo_weight < 12:
        truck += cargo_weight
        total_price += cargo_weight * 175
    else:
        train += cargo_weight
        total_price += cargo_weight * 120

average_price = total_price / total_weight

print(f'{average_price:.2f}')
print(f'{bus / total_weight * 100:.2f}%')
print(f'{truck / total_weight * 100:.2f}%')
print(f'{train / total_weight * 100:.2f}%')