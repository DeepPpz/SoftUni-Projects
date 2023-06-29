def even_odd_filter(**nums_dict):
    if "even" in nums_dict:
        nums_dict["even"] = [x for x in nums_dict["even"] if x % 2 == 0]
    if "odd" in nums_dict:
        nums_dict["odd"] = [x for x in nums_dict["odd"] if x % 2 != 0]

    return dict(sorted(nums_dict.items(), key=lambda x: -len(x[1])))
