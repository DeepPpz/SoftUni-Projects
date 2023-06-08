import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')

while True:
    line = input().split('-')
    action = line[0]

    if action == 'End':
        break

    elif action == 'Create':
        file = open(os.path.join(files_dir, f'{line[1]}'), 'w')
        file.close()

    elif action == 'Add':
        with open(os.path.join(files_dir, f'{line[1]}'), 'a') as file:
            file.write(f'{line[2]}\n')

    elif action == 'Replace':
        try:
            with open(os.path.join(files_dir, f'{line[1]}'), 'r+') as file:
                text = file.read().replace(line[2], line[3])
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print('An error occurred')

    elif action == 'Delete':
        file_path = os.path.join(files_dir, f'{line[1]}')
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print('An error occurred')
