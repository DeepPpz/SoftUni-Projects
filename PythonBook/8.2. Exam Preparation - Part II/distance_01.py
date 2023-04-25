speed = int(input())
first_time = int(input()) / 60
second_time = int(input()) / 60
third_time = int(input()) / 60

total_distance = speed * first_time
speed *= 1.10
total_distance += speed * second_time
speed *= 0.95
total_distance += speed * third_time

print(f"{total_distance:.2f}")
