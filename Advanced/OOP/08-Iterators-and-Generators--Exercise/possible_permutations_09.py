from itertools import permutations


def possible_permutations(numbers):
    for el in permutations(numbers):
        yield list(el)
