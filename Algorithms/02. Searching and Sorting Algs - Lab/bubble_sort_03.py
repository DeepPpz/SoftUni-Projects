def bubble_sort(i, nums):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(1, i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                is_sorted = False
        i -= 1


nums = [int(x) for x in input().split()]
i = len(nums)

bubble_sort(i, nums)
print(*nums, sep=' ')
