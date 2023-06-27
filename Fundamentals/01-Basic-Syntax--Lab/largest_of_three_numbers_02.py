num_one = int(input())
num_two = int(input())
num_three = int(input())

if num_one > num_two > num_three:
    print(num_one)
elif num_one < num_two > num_three:
    print(num_two)
else:
    print(num_three)
