n = int(input())
longest_intersection = []

for _ in range(n):
    first_range, second_range = [tuple(int(y) for y in x.split(',')) for x in input().split('-')]
    first_set = set([int(x) for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([int(x) for x in range(second_range[0], second_range[1] + 1)])

    curr_intersection = first_set.intersection(second_set)
    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = list(curr_intersection)

longest_intersection = list(sorted(longest_intersection))

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
