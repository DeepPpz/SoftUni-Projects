numbers = tuple(map(float, input().split()))
occurrences_data = {}

for i in range(len(numbers)):
    try:
        occurrences_data[numbers[i]] += 1
    except KeyError:
        occurrences_data[numbers[i]] = 1

for (num, occur) in occurrences_data.items():
    print(f"{num} - {occur} times")
