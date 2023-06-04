import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'my_first_file.txt')

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')
