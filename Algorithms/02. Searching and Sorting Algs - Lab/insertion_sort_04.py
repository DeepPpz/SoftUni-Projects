def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1


nums = [int(x) for x in input().split()]

insertion_sort(nums)
print(*nums, sep=' ')
