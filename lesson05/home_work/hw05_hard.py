# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("ping - тестовый ключ")
    print("ls - отображение полного пути текущей директории")
    print("mkdir <arg_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")


def make_dir():
    if not arg_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), arg_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(arg_name))
    except FileExistsError:
        print('директория {} уже существует'.format(arg_name))


def ping():
    print("pong")

def cp():
    if not arg_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copy2(arg_name, arg_name + "(copy)")
        print("%s скопирован" % arg_name)
    except Exception as e:
        print("%s не может быть скопирован")
    

def rm():
    if not arg_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.remove(arg_name)
        print("%s удалён" % arg_name)
    except Exception as e:
        print("%s не может быть удалён" % arg_name)

def cd():
    if not arg_name:
        print("Необходимо указать путь к папке вторым параметром")
        return
    try:
        os.chdir(arg_name)
        print("Перешел в папку %s" % os.getcwd())
    except Exception as e:
        print("Нельзя перейти в папку %s")

def ls():
    print(os.getcwd())


if __name__ == '__main__':

    do = {
        "help": print_help,
        "mkdir": make_dir,
        "ping": ping,
        "cp": cp,
        "rm": rm,
        "cd": cd,
        "ls": ls
    }

    try:
        arg_name = sys.argv[2]
    except IndexError:
        arg_name = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None


    if key and do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")