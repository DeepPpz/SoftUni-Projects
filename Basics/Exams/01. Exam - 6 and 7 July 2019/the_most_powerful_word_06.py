import math

vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
max_word = ""
max_power = 0

while True:
    curr_word = input()
    curr_power = 0
    if curr_word == "End of words":
        break

    for letter in curr_word:
        curr_power += ord(letter)

    if curr_word[0] in vowels:
        curr_power *= len(curr_word)
    else:
        curr_power = math.floor(curr_power / len(curr_word))

    if curr_power >= max_power:
        max_word = curr_word
        max_power = curr_power

print(f"The most powerful word is {max_word} - {max_power}")
