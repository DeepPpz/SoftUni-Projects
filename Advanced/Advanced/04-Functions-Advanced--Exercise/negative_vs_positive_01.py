def separate_numbers(nums):
    positive_nums = []
    negative_nums = []
    for n in nums:
        if n < 0:
            negative_nums.append(n)
        else:
            positive_nums.append(n)

    sum_positive, sum_negative = sum(positive_nums), sum(negative_nums)
    print(f"{sum_negative}\n{sum_positive}")
    if abs(sum_negative) > sum_positive:
        print(f"The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
separate_numbers(numbers)
