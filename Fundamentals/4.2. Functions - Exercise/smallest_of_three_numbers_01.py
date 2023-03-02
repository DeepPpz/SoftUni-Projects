def find_smallest(one, two, three):
    if one < two and one < three:
        return one
    elif two < one and two < three:
        return two
    else:
        return three


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(find_smallest(first_num, second_num, third_num))