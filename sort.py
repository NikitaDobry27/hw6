import re
import os




def normalize(string:str) -> str:
    
    if not isinstance(string, str):
        return None

    
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }

    translit_string = ''
    for char in string:
        if char in translit_dict:
            translit_string += translit_dict[char]
        else:
            translit_string += char

    
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

def process_images(path:str) -> dict:
    image_filenames = []



def process_videos(file_path):
    pass

def process_documents(file_path):
    pass

def process_music(file_path):
    pass

def process_archives(file_path):
    pass

def process_unknown(file_path):
    pass

