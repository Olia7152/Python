# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.

import pathlib
from collections import namedtuple

DIRSUBJECT = namedtuple('DIRSUBJECT',['file_name', 'ext', 'flag', 'parent'])

def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
    return new_list

print(dir_info('D:\GB\Погружение в пайтон\HW_python\HW_15'))