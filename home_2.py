# Задачи на логические выражения и условный оператор if.

# task num_1
# Запрашиваем у пользователя число
number = int(input("Введите число: "))

# Проверяем последнюю цифру
if number % 10 == 3:
    print(True)
else:
    print(False)

# task num_2
# Ввод чисел с клавиатуры в одной строке
number_1, number_2, number_3 = map(int, input("Введите три числа через пробел: ").split())

# Проверка наличия отрицательных чисел
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print(True)
else:
    print(False)

# task num_3
# Ввод двух чисел
number_1, number_2 = map(int, input("Введите два числа через пробел: ").split())

# Проверка одинаковой четности
if number_1 % 2 == number_2 % 2:
    print(True)
else:
    print(False)

# task num_4
# Ввод трех сторон треугольника
side_a, side_b, side_c = map(int, input("Введите три стороны треугольника через пробел: ").split())

# Определение типа треугольника
if side_a == side_b == side_c:
    print("equilateral")  # Равносторонний треугольник
else:
    if side_a == side_b or side_a == side_c or side_b == side_c:
        print("isosceles")  # Равнобедренный треугольник
    else:
        print("scalene")  # Разносторонний треугольник

# task num_5
# Ввод трех чисел
number_1, number_2, number_3 = map(int, input("Введите три числа через пробел: ").split())

# Инициализация счетчика четных чисел
even_count = 0

# Проверка четности первого числа
if number_1 % 2 == 0:
    even_count += 1

# Проверка четности второго числа
if number_2 % 2 == 0:
    even_count += 1

# Проверка четности третьего числа
if number_3 % 2 == 0:
    even_count += 1

# Вывод количества четных чисел
print(even_count)

# task num_6
# Ввод двузначного числа
number = int(input("Введите двузначное число: "))

# Извлечение десятков и единиц
tens = number // 10  # Десятки
ones = number % 10  # Единицы

# Сумма цифр числа
sum_of_digits = tens + ones

# Проверка, является ли сумма цифр двузначным числом
if sum_of_digits >= 10:
    if sum_of_digits <= 99:
        print("Сумма цифр двузначного числа является двузначным числом.")
    else:
        print("Сумма цифр двузначного числа не является двузначным числом.")
else:
    print("Сумма цифр двузначного числа не является двузначным числом.")

# task num_7
# Ввод четырёхзначного числа
number = input("Введите четырёхзначное число: ")

# Проверка, что все цифры одинаковы
if number[0] == number[1] == number[2] == number[3]:
    print("Все цифры одинаковы.")
else:
    print("Цифры не одинаковы.")

# task num_8
# Ввод года
year = int(input("Введите год: "))

# Проверка на високосность
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Не високосный")
else:
    print("Не високосный")

# Цикл   For  задачи с числами.

# task number_1
# Цикл for, который выводит число "10" 20 раз
for _ in range(20):
    print(10)

# task number_2
# Ввод значений start и stop
start = int(input("Введите начало диапазона (start): "))
stop = int(input("Введите конец диапазона (stop): "))

# Цикл for, который выводит все числа от start до stop
for number in range(start, stop + 1):
    print(number)

# task number_3
# Цикл for, который выводит числа от 100 до -100 включительно
for number in range(100, -101, -1):
    print(number, end=" ")

# task number_4
# Инициализация переменной для хранения суммы
total_sum = 0

# Цикл for, который перебирает числа от 100 до 500
for number in range(100, 501):
    total_sum += number

# Вывод суммы
print(total_sum)

# task number_5
# Инициализация переменной для хранения произведения
product = 1

# Цикл for, который перебирает числа от 5 до 20
for number in range(5, 21):
    product *= number

# Вывод произведения
print(product)

# task number_6
# Ввод числа n
n = int(input("Введите натуральное число n: "))

# Инициализация переменной для хранения факториала
factorial = 1

# Цикл for, который перебирает числа от 1 до n
for i in range(1, n + 1):
    factorial *= i  # Умножаем на текущее число

# Вывод факториала
print(f"Факториал числа {n} = {factorial}")
