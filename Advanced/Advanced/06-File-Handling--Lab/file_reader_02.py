import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'numbers.txt')

numbers_file = open(file_path, 'r')
sum_numbers = 0

for num in numbers_file:
    sum_numbers += int(num)
print(sum_numbers)
