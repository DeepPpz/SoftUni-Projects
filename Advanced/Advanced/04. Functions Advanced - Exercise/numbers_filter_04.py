def even_odd_filter(**nums_dict):
    if "even" in nums_dict:
        nums_dict["even"] = [x for x in nums_dict["even"] if x % 2 == 0]
    if "odd" in nums_dict:
        nums_dict["odd"] = [x for x in nums_dict["odd"] if x % 2 != 0]

    return dict(sorted(nums_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))
