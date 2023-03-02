pokemons = [int(x) for x in input().split()]
total_sum = 0

while len(pokemons) > 0:
    idx = int(input())
    value = 0

    if idx < 0:
        value = pokemons[0]
        pokemons.pop(0)
        pokemons.insert(0, pokemons[len(pokemons) - 1])

    elif idx >= len(pokemons):
        value = pokemons[len(pokemons) - 1]
        pokemons.pop(len(pokemons) - 1)
        pokemons.append(pokemons[0])

    else:
        value = pokemons[idx]
        pokemons.pop(idx)

    for i in range(len(pokemons)):
        if pokemons[i] <= value:
            pokemons[i] += value
        else:
            pokemons[i] -= value
    total_sum += value

print(total_sum)