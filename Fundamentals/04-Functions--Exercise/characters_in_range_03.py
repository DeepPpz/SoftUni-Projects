def find_characters_in_range(a, b):
    chars = []
    for i in range(ord(a) + 1, ord(b)):
        chars.append(chr(i))
    return chars


first_char = input()
second_char = input()

result = find_characters_in_range(first_char, second_char)
print(*result, sep=' ')
