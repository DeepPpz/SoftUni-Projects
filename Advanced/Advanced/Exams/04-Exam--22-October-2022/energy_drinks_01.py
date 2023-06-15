from collections import deque

all_caffeine = deque([int(x) for x in input().split(', ')])
all_energy_drinks = deque([int(x) for x in input().split(', ')])
MAX_CAFFEINE = 300

caffeine_taken = 0
while all_caffeine and all_energy_drinks:
    caffeine = all_caffeine.pop()
    energy_drink = all_energy_drinks.popleft()
    curr_caffeine = caffeine * energy_drink

    if caffeine_taken + curr_caffeine <= MAX_CAFFEINE:
        caffeine_taken += curr_caffeine
    else:
        all_energy_drinks.append(energy_drink)
        if caffeine_taken >= 30:
            caffeine_taken -= 30
        else:
            caffeine_taken = 0

if all_energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in all_energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f'Stamat is going to sleep with {caffeine_taken} mg caffeine.')
