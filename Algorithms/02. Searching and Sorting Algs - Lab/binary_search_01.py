def binary_search(target, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = array[mid_idx]

        if mid_el == target:
            return mid_idx
        elif mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


array = [int(x) for x in input().split()]
target = int(input())

print(binary_search(target, array))





# recursive solution

# def binary_search(left, right, array):
#     if left > right:
#         print("-1")
#         return
#
#     mid_idx = (left + right) // 2
#     mid_el = array[mid_idx]
#
#     if mid_el == target:
#         print(mid_idx)
#     elif mid_el < target:
#         binary_search(mid_idx +1, right, array)
#     else:
#         binary_search(left, mid_idx - 1, array)
#
#
# array = [int(x) for x in input().split()]
# target = int(input())
#
# binary_search(0, len(array) - 1, array)
