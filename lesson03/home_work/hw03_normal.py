# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibo_list = [1, 1]
    for i in range(m):
        count = len(fibo_list) - 2
        last = len(fibo_list) - 1
        fibo_list.append(fibo_list[count] + fibo_list[last])
    return fibo_list[n:m+1]

print(fibonacci(1, 9))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    start = origin_list[:]
    res = []

    while len(start) > 0:

        lesser = start[0]

        for i in range(len(start)):
            if start[i] <= lesser:
                lesser = start[i]
        res.append(lesser)
        start.remove(lesser)


    return res

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# Не ясно, какой именно фильтр надо было написать?
# Т.е. я понял, как именно ф-ия фильтр работает, но что именно написать - не понял.

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Задание не совсем понятно


input()