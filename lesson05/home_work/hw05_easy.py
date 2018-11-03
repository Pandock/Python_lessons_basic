# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# import os
# import sys

#Создаем нужное количество папок dir:

# def createFolder(directory, count):
#     for i in range(1, count + 1):
#         os.mkdir(directory[:-1] + str(i) + directory[-1])

# createFolder('./dir_/', 9)

# print(os.listdir('.'))

# #Removing empty dir_ folders:

# def remove_dir():
#     dirs = os.listdir('.')
#     for i in range(len(dirs)):
#         if 'dir_' in dirs[i]:
#             os.rmdir(dirs[i])

# remove_dir()

# print(os.listdir('.'))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def curr_dir_files():
    from os import listdir, path
    res = [i for i in listdir() if path.isdir(i)]
    # print(res)
    return res


print(curr_dir_files())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# def file_copy ():
#     from shutil import copy
#     from os import path
#     dest = path.basename(__file__)
#     copy(dest, dest + '_copy')
#     if path.exists(__file__ + '_copy'):
#         print('Копия текущего файла успешно создана')
#     else:
#         print('Что-то пошло не так')
#
#
# file_copy()
#

