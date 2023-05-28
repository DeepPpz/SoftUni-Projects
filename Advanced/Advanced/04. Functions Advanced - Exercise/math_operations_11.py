def math_operations(*args, **letters_data):
    for i in range(len(args)):
        el_idx = (i + 1) % 4
        if el_idx % 4 == 0:
            letters_data['m'] *= args[i]
        elif el_idx % 3 == 0:
            if args[i] != 0:
                letters_data['d'] /= args[i]
        elif el_idx % 2 == 0:
            letters_data['s'] -= args[i]
        else:
            letters_data['a'] += args[i]

    sorted_letters = dict(sorted(letters_data.items(), key= lambda x: (-x[1], x[0])))
    result = ""
    for (key, value) in sorted_letters.items():
        result += f"{key}: {value:.1f}\n"
    return result
