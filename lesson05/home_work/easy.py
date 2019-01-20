import os

def ls():
    print("Каталоги и файлы директории:")
    print(os.listdir('.'))

def cd(path):
    try:
        os.chdir(path)
        print("Успешно перешел перейти")
        print(os.getcwd())
    except Exception as e:
        print("Невозможно перейти")
    
def rmdir(name):
    try:
        os.rmdir(name)
        print("Папка %s удалена" % name)
    except Exception as e:
        print("Нельзя просто так взять и удалить папку %s" % name)
    

def mkdir(name):
    try:
        os.mkdir(name)
        print("Папка %s успешно создана" % name)
    except Exception as e:
        print("Нельзя просто так взять и создать папку %s" % name)