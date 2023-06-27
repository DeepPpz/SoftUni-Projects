prev_year = int(input())

next_year = prev_year + 1

while True:
    if len(list(str(next_year))) == len(set(str(next_year))):
        print(next_year)
        exit()
    else:
        next_year += 1
