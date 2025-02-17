class RangeSquared:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


for num in RangeSquared(2, 14):
    print(num)


########################################################################################################################

def factorial_gen(n):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

    for i in range(n + 1):
        yield factorial(i)


for fact in factorial_gen(4):
    print(fact)

#0r
import math
def factorial_gen(n):
    for i in range(n + 1):
        yield math.factorial(i)  # Используем math.factorial для улучшения производительности

for fact in factorial_gen(4):
    print(fact)

########################################################################################################################

def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()  # Убираем лишние пробелы и символы новой строки


for line in read_file_lines('filename.txt'):
    print(line)


########################################################################################################################

def calculate_complex_formula(a, b, c, d, e, f, g, h):
    result = 0

    # Первая часть формулы
    if a > 0:
        result += b * c
    else:
        result -= d / e

    # Вторая часть формулы
    if g < h:
        result += f * (g + h)
    else:
        result -= (d - f) / g

    return result


print(calculate_complex_formula(1, 2, 3, 4, 5, 6, 7, 8))
########################################################################################################################

class User:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    def greet(self):
        if self.age >= 18:
            print(f"Привет, {self.name}! Добро пожаловать на сайт для взрослых.")
        else:
            print(f"Привет, {self.name}! Добро пожаловать на детский сайт.")


# Пример использования
user1 = User("Алекс", 25)
user1.greet()

user2 = User("Лиза", 12)
user2.greet()
