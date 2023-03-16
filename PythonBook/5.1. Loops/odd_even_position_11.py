# Created by: Georgi Tashev AKA xaoccc

# input
inputs_count = int(input())
number_sum_even = 0
number_sum_odd = 0
max_num_even = -100000.00
max_num_odd = -100000.00
min_num_even = 100000.00
min_num_odd = 100000.00

# logic
for i in range(1, inputs_count + 1):
    number = float(input())
    if i % 2 == 0:
        number_sum_even += number
        if number > max_num_even:
            max_num_even = number
        if number < min_num_even:
            min_num_even = number
    elif i % 2 != 0:
        number_sum_odd += number
        if number > max_num_odd:
            max_num_odd = number
        if number < min_num_odd:
            min_num_odd = number

if number_sum_odd != 0:
    if number_sum_odd.is_integer():
        number_sum_odd = int(number_sum_odd)
if number_sum_even != 0:
    if number_sum_even.is_integer():
        number_sum_even = int(number_sum_even)
if min_num_odd != 0:
    if min_num_odd.is_integer():
        min_num_odd = int(min_num_odd)
if max_num_odd != 0:
    if max_num_odd.is_integer():
        max_num_odd = int(max_num_odd)
if min_num_even != 0:
    if min_num_even.is_integer():
        min_num_even = int(min_num_even)
if max_num_even != 0:
    if max_num_even.is_integer():
        max_num_even = int(max_num_even)

number_sum_odd_print = f"OddSum={number_sum_odd},"
number_sum_even_print = f"EvenSum={number_sum_even},"
min_num_odd_print = f"OddMin={min_num_odd},"
max_num_odd_print = f"OddMax={max_num_odd},"
min_num_even_print = f"EvenMin={min_num_even},"
max_num_even_print = f"EvenMax={max_num_even}"
if inputs_count == 1:
    min_num_even_print = "EvenMin=No,"
    max_num_even_print = "EvenMax=No"
elif inputs_count == 0:
    min_num_even_print = "EvenMin=No,"
    max_num_even_print = "EvenMax=No"
    min_num_odd_print = "OddMin=No,"
    max_num_odd_print = "OddMax=No,"

# print output
print(number_sum_odd_print)
print(min_num_odd_print)
print(max_num_odd_print)
print(number_sum_even_print)
print(min_num_even_print)
print(max_num_even_print)
