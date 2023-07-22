from datetime import date as datetype
from datetime import timedelta

first_year = int(input())
second_year = int(input())
wanted_num = int(input())

curr_date = datetype(first_year, 1, 1)
found = False

while curr_date.year <= second_year:
    d1 = curr_date.day // 10
    d2 = curr_date.day % 10
    d3 = curr_date.month // 10
    d4 = curr_date.month % 10
    d5 = curr_date.year // 1000
    d6 = (curr_date.year // 100) % 10
    d7 = (curr_date.year // 10) % 10
    d8 = curr_date.year % 10

    weight = d1 * (d2 + d3 + d4 + d5 + d6 + d7 + d8) + \
             d2 * (d3 + d4 + d5 + d6 + d7 + d8) + d3 * (d4 + d5 + d6 + d7 + d8) + \
             d4 * (d5 + d6 + d7 + d8) + d5 * (d6 + d7 + d8) + d6 * (d7 + d8) + d7 * d8

    if weight == wanted_num:
        found = True
        print(f"{d1}{d2}-{d3}{d4}-{d5}{d6}{d7}{d8}")

    curr_date += timedelta(days=1)

if not found:
    print("No")
