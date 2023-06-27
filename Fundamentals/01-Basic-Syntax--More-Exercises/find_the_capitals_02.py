word = input()

i = 0
index_list = list(range(len(word)))

for char in word:
    if not 65 <= ord(char) <= 90:
        index_list.remove(i)
    i += 1

print(index_list)
