import math

num_people = int(input())
capacity = int(input())

courses = math.ceil(num_people / capacity)

print(courses)
