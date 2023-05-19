# not in Judge

numbers_list = list(map(int, input().split()))
target_num = int(input())

targets = set()
values_dict = {}

for num in numbers_list:
    if num not in targets:
        result = target_num - num
        targets.add(result)
        values_dict[result] = num
    else:
        targets.remove(num)
        m = values_dict[num]
        del values_dict[num]
        print(f"{m} + {num} = {target_num}")
