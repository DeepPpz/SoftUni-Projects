n = int(input())
sum_evens = 0
sum_odds = 0
max_even = -10000000000000.00
max_odd = -10000000000000.00
min_even = 10000000000000.00
min_odd = 10000000000000.00

for i in range(1, n + 1):
    num = float(input())
    
    if i % 2 == 0:
        sum_evens += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    
    else:
        sum_odds += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num

if sum_odds != 0 and sum_odds.is_integer():
    sum_odds = int(sum_odds)
if sum_evens != 0 and sum_evens.is_integer():
    sum_evens = int(sum_evens)
if min_odd != 0 and min_odd.is_integer():
    min_odd = int(min_odd)
if max_odd != 0 and max_odd.is_integer():
    max_odd = int(max_odd)
if min_even != 0 and min_even.is_integer():
    min_even = int(min_even)
if max_even != 0 and max_even.is_integer():
    max_even = int(max_even)

print(f"OddSum={sum_odds},")
if n == 0:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={min_odd},")
    print(f"OddMax={max_odd},")

print(f"EvenSum={sum_evens},")
if n <= 1:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={min_even},")
    print(f"EvenMax={max_even}")
