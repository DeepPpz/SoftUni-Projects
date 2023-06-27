animals = input().split(', ')

animals.append('you')
animals.reverse()

wolf_ind = animals.index('wolf')

if wolf_ind == 1:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number %d! You are about to be eaten by a wolf!' % (wolf_ind - 1))
