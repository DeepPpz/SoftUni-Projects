def sum_array(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + sum_array(numbers, idx + 1)


numbers = [int(x) for x in input().split()]
print(sum_array(numbers, 0))
