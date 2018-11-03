import os
import sys
import shutil


def create_folder(directory, count):
    for i in range(1, count + 1):
        os.mkdir(directory + str(i))
    print(curr_dir_files())


def remove_dir():
    dirs = os.listdir('.')
    for i in range(len(dirs)):
        if 'dir_' in dirs[i]:
            os.rmdir(dirs[i])


def curr_dir_files():
    from os import listdir, path
    res = [i for i in listdir() if path.isdir(i)]
    # print(res)
    return res


def file_copy ():
    from shutil import copy
    from os import path
    dest = path.basename(__file__)
    copy(dest, dest + '_copy')
    if path.exists(__file__ + '_copy'):
        print('Копия текущего файла успешно создана')
    else:
        print('Что-то пошло не так')
