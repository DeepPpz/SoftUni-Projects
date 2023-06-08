import os
from string import punctuation

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'text.txt')

with open(file_path, 'r') as file:
    curr_text = file.readlines()

output = []
for i in range(len(curr_text)):
    letters = sum([1 for x in curr_text[i] if x.isalpha()])
    symbols = sum([1 for x in curr_text[i] if x in punctuation])
    line = curr_text[i].rstrip('\n')
    output.append(f'Line {i+1}: {line} ({letters})({symbols})')

new_file_path = os.path.join(files_dir, 'output.txt')
with open(new_file_path, 'w') as file:
    for line in output:
        print(line)
        file.write(f'{line}\n')
