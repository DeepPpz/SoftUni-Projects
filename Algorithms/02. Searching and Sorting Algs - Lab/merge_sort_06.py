def merge_arrays(left, right):
    sorted_array = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_array.append(left[left_idx])
            left_idx += 1
        else:
            sorted_array.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        sorted_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_array.append(right[right_idx])
        right_idx += 1

    return sorted_array


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]
    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(x) for x in input().split()]

sorted_nums = merge_sort(nums)
print(*sorted_nums, sep=' ')
