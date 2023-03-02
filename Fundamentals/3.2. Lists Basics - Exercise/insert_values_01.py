string_numbers = input().split()

opposite_num = []

for i in range(len(string_numbers)):
    opposite_num.append(-int(string_numbers[i]))

print(opposite_num)