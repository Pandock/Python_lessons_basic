
__author__ = 'Тошматов Д. Д.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = list(input("Введите число: "))

i = 0
maxNum = 0

while i < len(x):
    elemX = int(x[i])
    if elemX >= maxNum:
        maxNum = elemX
        i += 1
    else:
        i += 1

print(maxNum)

print("А теперь второй способ:")

for i in x:
    if int(i) >= int(maxNum):
        maxNum = i

print(maxNum)
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.



# first = tuple(input('Введите '))


# x = input("Введите первую переменную: ")
# y = input("Введите вторую переменную: ")



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите первый коэффициент a: '))
b = int(input('Введите второй коэффициент b: '))
c = int(input('Введите свободный член с: '))

D = (b ** 2) - 4 * (a * c)

if D != 0:
    xFirst = (-b + math.sqrt(D)) / (2 * a)
    xSec = (-b - math.sqrt(D)) / (2 * a)

    print('Первый корень равен', xFirst, ', второй корень равен', xSec)
else:
    print("D < 0, корней нет")

input()