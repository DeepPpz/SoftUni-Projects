import os


def find_files(files_dir, base_case=False):
    total_files = os.listdir(files_dir)

    for file in total_files:
        curr_path = os.path.join(files_dir, file)

        if os.path.isfile(curr_path):
            extension = file.split('.')[-1]

            if extension not in files_data:
                files_data[extension] = []
            files_data[extension].append(file)

        elif not base_case:
            find_files(curr_path, base_case=True)


directory = input()
files_data = {}
find_files(directory)

sorted_data = dict(sorted(files_data.items(), key=lambda x: x[0]))
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files', 'report.txt')

with open(report_path, 'w') as report:
    for (key, values) in sorted_data.items():
        report.write(f'.{key}\n')
        for file in sorted(values):
            report.write(f'- - - {file}\n')
