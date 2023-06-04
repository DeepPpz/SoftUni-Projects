import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file = open(os.path.join(files_dir, 'my_first_file.txt'), 'w')

file.write('I just created my first file!')
file.close()
