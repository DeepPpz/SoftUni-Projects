collected_sum = 0

while True:
    destination = input()

    if destination == 'End':
        break

    min_budget = float(input())

    while True:
        curr_sum = float(input())
        collected_sum += curr_sum

        if collected_sum >= min_budget:
            print(f'Going to {destination}!')
            collected_sum = 0
            break
