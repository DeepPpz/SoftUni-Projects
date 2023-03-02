numbers = [int(num) for num in input().split(', ')]

group, curr_list = 0, []

while len(numbers) > 0:
    group += 10

    curr_list = [el for el in numbers if el <= group]
    print(f"Group of {group}'s: {curr_list}")
    numbers = list(filter(lambda x: x not in curr_list, numbers))