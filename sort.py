
import os
import shutil
import sys
from normalize import normalize
from formats import formats


known_formats = set()
unknown_formats = set()
RESULT = []


def rename_folders(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isdir(file_path):
            rename_folders(file_path)
            new_foldername = normalize(filename)
            if new_foldername != filename:
                new_folder_path = os.path.join(path, new_foldername)
                if not os.listdir(file_path):
                    os.rename(file_path, new_folder_path)
                   
                
                else:
                    shutil.move(file_path, new_folder_path)
        else:
            name, ext = os.path.splitext(filename)
            new_filename = normalize(name) + ext
            new_file_path = os.path.join(path, new_filename)
            os.rename(file_path, new_file_path)
            
    
         



def get_file_extension(file_path):

    return os.path.splitext(file_path)[1].strip('.')

def get_directory_name(file_extension):

    for directory, extensions in formats.items():
        if file_extension.upper() in extensions:
            return directory
    return None

def create_directory(file_path):
    for category in formats.keys():
        folder_path = os.path.join(file_path, category)
        os.makedirs(folder_path, exist_ok=True)

def get_file_name_without_extension(filename):
    return os.path.splitext(filename)[0]

def move_file(file_path, target_directory_path):
    filename = os.path.basename(file_path)
    if not filename.startswith('.'):
        shutil.move(file_path, target_directory_path)

def sort_files(folder_path):
    files_by_category = {category: [] for category in formats.keys()}
    archive_extensions = formats['archives']

    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_extension = get_file_extension(file_path)
            moved = False
            if file_extension.upper() in archive_extensions:
                directory_path = os.path.join(folder_path, 'archives')
                known_formats.add(file_extension)
                archive_path = os.path.join(dirpath, filename)
                target_dir_path = os.path.join(directory_path, get_file_name_without_extension(filename))
                RESULT.append(filename)
                shutil.unpack_archive(archive_path, target_dir_path)
                sort_files(target_dir_path)  
                moved = True
            else:
                for category, extensions in formats.items():
                    if file_extension.upper() in extensions:
                        files_by_category[category].append(file_path)
                        known_formats.add(file_extension)
                        directory_path = os.path.join(folder_path, category)
                        target_file_path = os.path.join(directory_path, filename)
                        RESULT.append(filename)
                        move_file(file_path, target_file_path)
                        moved = True
                        break
            if not moved:
                unknown_formats.add(file_extension)

def remove_empty_folders(folder_path):
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for dirname in dirnames:
            if dirname not in formats.keys():
                directory_path = os.path.join(dirpath, dirname)
                if not os.listdir(directory_path):
                    if not any(dirname in s for s in formats.values()):
                        os.rmdir(directory_path)

def final_sort(path):
    rename_folders(path)
    create_directory(path)
    sort_files(path)
    remove_empty_folders(path)

if __name__ == '__main__':
    PATH_TO_FOLDER = sys.argv[1]
    if os.path.exists(PATH_TO_FOLDER):
        try:
            final_sort(PATH_TO_FOLDER)
            print('Перенесені файли:')
            print('\n'.join(RESULT))
            print('\n')

            print('Відомі формати:')
            print(', '.join(known_formats))
            print('\n')

            print('Невідомі формати:')
            print(', '.join(unknown_formats))
        except PermissionError:
            print('Permission error occured')
    
