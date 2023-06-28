removed_word = input()
sequence = input()

while removed_word in sequence:
    sequence = sequence.replace(removed_word, "")

print(sequence)
