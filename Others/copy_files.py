import os
import shutil

def search_and_copy_pictures(source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination, file)
                shutil.copy2(source_path, destination_path)


source_folder = 'C:\\Users\\Dessy\\Pictures\\Discord'
destination_folder = 'C:\\Users\\Dessy\\Desktop\\New folder'

search_and_copy_pictures(source_folder, destination_folder)
