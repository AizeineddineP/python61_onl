words = input().split()
sorted_words = sorted(words, key=len, reverse=True)
print(*sorted_words)

words = input().split()
sorted_words = sorted(words, key=lambda word: word.count('a'))
print(*sorted_words)

# Шаг 1: Создаём словарь с количеством учащихся в классах
school = {
    '9а': 25,
    '9б': 27,
    '9в': 23,
    '9м': 30,
    '9ф': 22
}

# Шаг 2: Изменение количества учащихся в одном из классов
school['9б'] = 26  # В классе 9б изменилось количество учащихся

# Шаг 3: Добавление нового класса
school['9г'] = 24  # Добавили новый класс 9г

# Шаг 4: Удаление расформированного класса
del school['9в']  # Удалили класс 9в

# Шаг 5: Вычисление общего количества учащихся
total_students = sum(school.values())  # Суммируем значения учащихся по всем классам

# Выводим результаты
print("Общее количество учащихся в 9 классах:", total_students)
print("Данные по классам:", school)


# НЕ ПОНЯЛ КАК СОЗДАТЬ ТАКОЙ ПРОГРАММЫ ДЛЯ ТЕЛЕФОНОВ И ИМЕН


def get_element(lst: list, index: int):
    try:
        return lst[index]  # Попытка вернуть элемент по индексу
    except IndexError:
        return "Ошибка: индекс вне диапазона"  # Если индекс вне диапазона


# Пример использования
lst = [10, 20, 30, 40, 50]
print(get_element(lst, 2))  # Вывод: 30
print(get_element(lst, 5))  # Вывод: Ошибка: индекс вне диапазона


def retry_on_exception(retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f"Ошибка: {e}. Повтор {attempt + 1}/{retries}")
            raise ValueError(f"Функция не удалась после {retries} попыток.")

        return wrapper

    return decorator


import threading

#####################################
def timeout(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [None]  # Используем список для хранения результата
            exception = [None]

            def target():
                try:
                    result[0] = func(*args, **kwargs)  # Выполняем функцию
                except Exception as e:
                    exception[0] = e  # Сохраняем исключение, если оно есть

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(limit)  # Ждём завершения, но не дольше limit секунд

            if thread.is_alive():  # Если поток не завершился за limit секунд
                raise TimeoutError(f"Функция превысила лимит {limit} секунд")

            if exception[0]:  # Если функция выбросила исключение, передаём его дальше
                raise exception[0]

            return result[0]  # Возвращаем результат функции

        return wrapper

    return decorator
#