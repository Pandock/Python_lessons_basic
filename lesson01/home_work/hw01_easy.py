
__author__ = 'Тошматов Д. Д.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

x = list(input("Введите число: "))

i = 0
while i < len(x):
	print(x[i])
	i += 1

print("А теперь второй способ:")

for i in x:
	print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите первую переменную: ")
b = input("Введите вторую переменную: ")

c = a

a = b
b = c

print("Новые значения: первая переменная =", a, ", вторая переменная =", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите ваш возраст: '))
minAge = 18

if age >= minAge:
	print('Доступ разрешен')
else:
	print('Извините, пользование данным ресурсом только с 18 лет')

input()