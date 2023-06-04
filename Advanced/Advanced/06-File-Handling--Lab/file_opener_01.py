import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'text.txt')

if os.path.isfile(file_path):
    print('File found')
else:
    print('File not found')
