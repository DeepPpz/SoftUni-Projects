def rounding(lists):
    new_list = []
    for i in range(len(lists)):
        new_list.append(round(lists[i]))
    return new_list


numbers = input().split()
numbers = list(map(float, numbers))

result = (rounding(numbers))
print(result)
