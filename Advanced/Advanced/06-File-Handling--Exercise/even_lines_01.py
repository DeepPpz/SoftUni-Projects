import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'text.txt')
all_symbols = ["-", ",", ".", "!", "?"]

with open(file_path, 'r') as file:
    curr_text = file.readlines()

for i in range(0, len(curr_text), 2):
    for sym in all_symbols:
        curr_text[i] = curr_text[i].replace(sym, '@')

    print(*reversed(curr_text[i].split()), sep=' ')
