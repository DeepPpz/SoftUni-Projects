first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

functions = {
    "Add First": lambda x: [first_sequence.add(el) for el in x],
    "Add Second": lambda x: [second_sequence.add(el) for el in x],
    "Remove First": lambda x: [first_sequence.discard(el) for el in x],
    "Remove Second": lambda x: [second_sequence.discard(el) for el in x],
    "Check Subset": lambda x: print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
}

for i in range(int(input())):
    line = input().split()
    command = ' '.join(line[0:2])

    functions[command](int(x) for x in line[2:])

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
