nums = [int(x) for x in input().split()]

average = sum(nums) / len(nums)
top_nums = [el for el in nums if el > average]

sorted_nums = sorted(top_nums, reverse=True)

if len(sorted_nums) == 0:
    print('No')
else:
    print(*sorted_nums[:5], sep=' ')
