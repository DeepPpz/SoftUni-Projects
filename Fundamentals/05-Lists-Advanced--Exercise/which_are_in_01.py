first_sequence = input().split(', ')
second_sequence = input().split(', ')

output_list = []

for f_el in first_sequence:
    for s_el in second_sequence:
        if f_el in s_el and f_el not in output_list:
            output_list.append(f_el)

print(output_list)
