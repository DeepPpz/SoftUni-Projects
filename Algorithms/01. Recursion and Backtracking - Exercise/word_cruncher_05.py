def find_word_combinations(idx, words_by_idx, words_count, curr_combination):
    if idx >= len(target_string):
        print(*curr_combination, sep=' ')
        return
    if idx not in words_by_idx:
        return

    for el in words_by_idx[idx]:
        if words_count[el] == 0:
            continue
        curr_combination.append(el)
        words_count[el] -= 1
        find_word_combinations(idx + len(el), words_by_idx, words_count, curr_combination)
        curr_combination.pop()
        words_count[el] += 1


elements = input().split(", ")
target_string = input()
words_by_idx = {}
words_count = {}

for el in elements:
    if el in words_count:
        words_count[el] += 1
        continue
    else:
        words_count[el] = 1

    try:
        idx = 0
        while True:
            idx = target_string.index(el, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(el)
            idx += len(el)
    except ValueError:
        pass

find_word_combinations(0, words_by_idx, words_count, [])
