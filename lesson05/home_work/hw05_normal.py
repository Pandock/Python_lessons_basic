# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil
import easy


def delete_folder():
    print(easy.curr_dir_files())
    rem_dir = input('Какую папку необходимо удалить? \n')
    if os.path.isdir(rem_dir):
        os.rmdir(rem_dir)
        if not os.path.isdir(rem_dir):
            print('Файл успешно удален')


answer = 'Y'

while answer.lower() == 'y':
    act = int(input('Выберите нужное действие:\n[1] - Перейти в папку\n[2] - Просмотреть содержимое текущей папки\n[3] - Удалить папку\n[4] - Создать папку\n'))

    if act == 1:
        print('Папки в текущей директории: ')
        for i in easy.curr_dir_files():
            print(i)
        path = input('Введите название папки:')
        os.chdir(path)
        fin_path = str(os.getcwd())
        print('Вы перешли в папку ' + fin_path)

    elif act == 2:
        print('Файлы в текущей директории: ')
        for i in os.listdir('.'):
            print(i)
    elif act == 3:
        delete_folder()
    elif act == 4:
        folder_name = input('Введите название для новой папки: ')
        folder_count = int(input('Введите необходимое количество копий: '))
        easy.create_folder(folder_name, folder_count)

    answer = input('Хотите продолжить работу? (Y/N): ')

