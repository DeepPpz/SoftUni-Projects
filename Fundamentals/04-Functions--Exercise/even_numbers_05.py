def filter_even_numbers(a):
    if a % 2 == 0:
        return True
    else:
        return False


sequence = [int(n) for n in input().split()]

filtered_list = filter(filter_even_numbers, sequence)
final_list = []

for el in filtered_list:
    final_list.append(el)

print(final_list)
