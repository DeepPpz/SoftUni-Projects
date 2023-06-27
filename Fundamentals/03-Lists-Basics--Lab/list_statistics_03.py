n = int(input())

positives, negatives = [], []
sum_negatives = 0

for i in range(n):
    curr_num = int(input())

    if curr_num >= 0:
        positives.append(curr_num)
    else:
        negatives.append(curr_num)
        sum_negatives += curr_num

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum_negatives}')
