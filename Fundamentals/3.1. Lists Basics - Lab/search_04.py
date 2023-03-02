n = int(input())
special_word = input()

string_list, clean_list = [], []

for s in range(n):
    curr_string = input()
    string_list.append(curr_string)
    if special_word in curr_string:
        clean_list.append(curr_string)

print(string_list)
print(clean_list)