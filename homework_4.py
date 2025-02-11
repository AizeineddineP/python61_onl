# Напишите функцию minimum вычисляющую минимум двух чисел.

# Определяем функцию
def minimum(a, b):
    return a if a < b else b


# Тестируем функцию
print(minimum(5, 10))  # Ожидаемый результат: 5
print(minimum(20, 10))  # Ожидаемый результат: 10
print(minimum(-5, -10))  # Ожидаемый результат: -10
print(minimum(0, 0))  # Ожидаемый результат: 0
print(minimum(7, 7))  # Ожидаемый результат: 7


# Найдите минимальное четырёх чисел с помощью функции написанной в предыдущей  задаче. Новую функцию не создавать!

# Использовать функцию из предыдущей задачи!
# Определяем функцию minimum
def minimum(a, b):
    return a if a < b else b


# Находим минимум из четырех чисел
def minimum_of_four(a, b, c, d):
    return minimum(minimum(a, b), minimum(c, d))


# Тестируем
print(minimum_of_four(10, 20, 5, 15))  # Ожидаемый результат: 5
print(minimum_of_four(-1, -5, -10, 0))  # Ожидаемый результат: -10
print(minimum_of_four(7, 7, 7, 7))  # Ожидаемый результат: 7

# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа и выведите результат работы этой функции.

import math


# Определяем функцию distance
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Читаем четыре числа от пользователя
x1, y1 = map(float, input("Введите координаты первой точки (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x2 y2): ").split())

# Вычисляем и выводим расстояние
result = distance(x1, y1, x2, y2)
print(f"Расстояние между точками: {result:.2f}")


# Дано натуральное число number > 1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, в противном случае

# не понял как!


# Напишите функцию fibbonachi которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# Ищем число Фиббоначи через цикл! Рекурсию не использовать!

def fibonacci(n):
    """
    Функция возвращает n-е число Фибоначчи.
    :param n: целое неотрицательное число
    :return: n-е число Фибоначчи
    """
    if n == 0:
        return 0  # Первое число Фибоначчи
    elif n == 1:
        return 1  # Второе число Фибоначчи

    # Начальные значения для последовательности
    a, b = 0, 1

    # Итеративно вычисляем числа Фибоначчи
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Пример использования
n = int(input("Введите неотрицательное число n: "))
print(f"{n}-е число Фибоначчи: {fibonacci(n)}")


# Напишите реализацию функции closest_mod_5,
# принимающую в качестве единственного аргумента целое число number и возвращающую самое маленькое целое число result,
# такое что:
# - result больше или равно number
# - result делится нацело на 5
# Попробуйте решить без цикла!

def closest_mod_5(number):
    """
    Функция возвращает наименьшее целое число, большее или равное number,
    которое делится нацело на 5.
    :param number: целое число
    :return: наименьшее число, удовлетворяющее условиям
    """
    # Если number уже делится на 5, возвращаем его
    if number % 5 == 0:
        return number
    # Иначе находим ближайшее число, увеличивая number до кратного 5
    return number + (5 - number % 5)


# Пример использования
n = int(input("Введите целое число: "))
print(f"Ближайшее число к {n}, делящееся на 5: {closest_mod_5(n)}")
