import re
import os
import shutil
import sys



def normalize(string:str) -> str:
    
    if not isinstance(string, str):
        return None

    
    translit_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
    'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ь': '', 'ю': 'iu', 'я': 'ia',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z',
    'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
    'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ь': '', 'Ю': 'Yu', 'Я': 'Ya',
}

    translit_string = string.translate(str.maketrans(translit_dict))
    pattern = re.compile(r'[^a-zA-Z0-9]')
    normalized_string = re.sub(pattern, '_', translit_string)

    return normalized_string


   
    
formats = {
        'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
        'video': ['AVI', 'MP4', 'MOV', 'MKV'],
        'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
        'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
        'archives': ['ZIP', 'GZ', 'TAR']
    }


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
                    print(f'{filename} has been renamed to {new_foldername}')
                else:
                    shutil.move(file_path, new_folder_path)
        else:
            name, ext = os.path.splitext(filename)
            new_filename = normalize(name) + ext
            new_file_path = os.path.join(path, new_filename)
            os.rename(file_path, new_file_path)
            print(f'{filename} has been renamed to {new_filename}')



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
            if file_extension.upper() in archive_extensions:
                directory_path = os.path.join(folder_path, 'archives')
         
                archive_path = os.path.join(dirpath, filename)
                target_dir_path = os.path.join(directory_path, get_file_name_without_extension(filename))
            
                shutil.unpack_archive(archive_path, target_dir_path)
                sort_files(target_dir_path)  
            else:
                for category, extensions in formats.items():
                    if file_extension.upper() in extensions:
                        files_by_category[category].append(file_path)
                        directory_path = os.path.join(folder_path, category)
                        target_file_path = os.path.join(directory_path, filename)
                        move_file(file_path, target_file_path)


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
        except PermissionError:
            print('Permission error occured')
    
