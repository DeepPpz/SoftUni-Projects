def reverse_list(idx, array):
    if idx < 0:
        return ' '.join(array)
    array.append(array[idx])
    array.pop(idx)
    return reverse_list(idx - 1, array)


array = input().split()
idx = len(array) - 1
print(reverse_list(idx, array))
