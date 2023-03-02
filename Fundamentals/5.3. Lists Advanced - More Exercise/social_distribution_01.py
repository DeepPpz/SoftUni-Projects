wealth = [int(x) for x in input().split(', ')]
min_wealth = int(input())

for i in range(len(wealth)):
    if wealth[i] < min_wealth:
        diff = min_wealth - wealth[i]
        if max(wealth) - diff >= min_wealth:
            idx = wealth.index(max(wealth))
            wealth[idx] -= diff
            wealth[i] += diff
        else:
            print('No equal distribution possible')
            exit()

print(wealth)