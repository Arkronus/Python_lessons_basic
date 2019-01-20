# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def mkdirs():
    for i in range(1,10):
        os.mkdir("dir_{}".format(i))

def rmdirs():
    for i in range(1,10):
        os.rmdir("dir_{}".format(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def lsdirs():
    path = '.'
    files = filter(lambda x: os.path.isdir(x), os.listdir(path))  
    print(list(files))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
def me():
    this_file = sys.argv[0]
    return os.path.join(os.getcwd(), this_file)

if __name__ == '__main__':
    print(me())