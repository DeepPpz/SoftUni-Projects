def find_odd_even_sum(a):
    odd_sum, even_sum = 0, 0
    for dig in a:
        curr_digit = int(dig)
        if curr_digit % 2 == 0:
            even_sum += curr_digit
        else:
            odd_sum += curr_digit

    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = input()

find_odd_even_sum(number)
