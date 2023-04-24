import math

total_bricks = int(input())
workers = int(input())
capacity = int(input())

total_courses = math.ceil(total_bricks / (workers * capacity))

print(total_courses)
