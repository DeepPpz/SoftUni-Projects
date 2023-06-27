count = int(input())

p1_count = 0  # < 200
p2_count = 0  # < 400
p3_count = 0  # < 600
p4_count = 0  # < 800
p5_count = 0  # >= 800

for i in range(count):
    number = int(input())
    if number < 200:
        p1_count += 1
    elif number < 400:
        p2_count += 1
    elif number < 600:
        p3_count += 1
    elif number < 800:
        p4_count += 1
    else:
        p5_count += 1

p1_perc = p1_count / count * 100
p2_perc = p2_count / count * 100
p3_perc = p3_count / count * 100
p4_perc = p4_count / count * 100
p5_perc = p5_count / count * 100

print(f'{p1_perc:.2f}%')
print(f'{p2_perc:.2f}%')
print(f'{p3_perc:.2f}%')
print(f'{p4_perc:.2f}%')
print(f'{p5_perc:.2f}%')
