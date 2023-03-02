import math

show_name = input()
duration = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
rest_time = break_time * 0.25
time_left = break_time - lunch_time - rest_time

if time_left >= duration:
    print(f"You have enough time to watch {show_name} and left with "
          f"{math.ceil(time_left - duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(duration - time_left)} more minutes.")