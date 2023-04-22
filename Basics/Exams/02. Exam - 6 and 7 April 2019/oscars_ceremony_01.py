rent = int(input())

statuettes = rent * 0.7
catering = statuettes * 0.85
sounding = catering / 2
total_expenses = rent + statuettes + catering + sounding

print(f"{total_expenses:.2f}")
