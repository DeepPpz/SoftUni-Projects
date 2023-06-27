deposit_sum = float(input())
period = int(input())
year_perc = float(input())

interest = deposit_sum * (year_perc / 100)
int_month = interest / 12
total_sum = deposit_sum + (period * int_month)

print(total_sum)
