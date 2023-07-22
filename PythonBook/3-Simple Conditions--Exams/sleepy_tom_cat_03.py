off_days = int(input())

work_days = 365 - off_days
norm = 30000

play_time = work_days * 63 + off_days * 127

diff = abs(norm - play_time)
hours = diff // 60
minutes = diff % 60

if play_time > norm:
    print("Tom will run away")
    print("{0} hours and {1} minutes more for play"
          .format(hours, minutes))
else:
    print("Tom sleeps well")
    print("{0} hours and {1} minutes less for play"
          .format(hours, minutes))