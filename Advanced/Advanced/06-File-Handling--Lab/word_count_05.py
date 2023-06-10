import os
import re


def read_content(file_path):
    with open(file_path, "r") as x:
        return x.read()


files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
searched_words_path = os.path.join(files_dir, 'words.txt')
scanned_file = os.path.join(files_dir, 'input.txt')

with open(searched_words_path, 'r') as file:
    searched_words = {key.lower(): 0 for key in file.read().split()}

with open(scanned_file, "r") as file:
    text_content = file.read()

words_list = re.findall(r'[A-Za-z]+', text_content.lower())

for word in words_list:
    if word in searched_words:
        searched_words[word] += 1

searched_words = dict(sorted(searched_words.items(), key=lambda x: -x[1]))

output_path = os.path.join(files_dir, 'output.txt')
with open(output_path, 'w') as file:
    for (word, count) in searched_words.items():
        file.write(f'{word} - {count}\n')
