off_days = int(input())

norm = 30000
work_norm = 63
off_norm = 127

work_days = 365 - off_days
total_play = work_days * work_norm + off_days * off_norm

if total_play > norm:
    print(f'Tom will run away')
    print(f'{(total_play - norm) // 60} hours and {(total_play - norm) % 60} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{(norm - total_play) // 60} hours and {(norm - total_play) % 60} minutes less for play')