import os

mode = "w"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open("input.txt", mode=mode) as file:
    file.write(" ".join(map(str, numbers)))

# r чтобы читать
with open("input.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

# произведение наших чисел от input.txt пусть будет result_numbers
result_numbers = 1
for num in numbers:
    result_numbers *= num

# создать output.txt и добавить туда наше произведение
with open("output.txt", "w") as file:
    file.write(str(result_numbers))
#####################################################################################################################################################

# создал json file чтобы оттуда все данные

# нужно от файла читать нащи данные
import json
from datetime import datetime  # чтобы узнать время

mode = "r"
encoding = "utf-8"
with open("products.json", mode=mode, encoding=encoding) as file:
    products = json.load(file)

# today
today = datetime.today()
date_format = "%d.%m.%Y"

# ищем среди наших продуктов типо как филтьр
filtered_products = []
# создаем условие через for
for product in products:
    name = product["name"]
    quantity = product["quantity"]
    price = product["price"]

    arrival_date = datetime.strptime(product["arrival_date"], date_format)  # дата поступления товара

    days_in_stock = (today - arrival_date).days  # сколько дней они у нас в магазине

    total_cost = quantity * price  # польная стоимость

    if days_in_stock > 30 and total_cost > 1_000_000:
        filtered_products.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "arrival_date": product["arrival_date"],
            "total_cost": total_cost
        })

if filtered_products:
    print("Товары, хранящиеся больше месяца и дороже 1 000 000 р:")
    for item in filtered_products:
        print(f"{item['name']} - {item['quantity']} шт. по {item['price']} р. "
              f"(Дата поступления: {item['arrival_date']}, Стоимость: {item['total_cost']} р.)")
else:
    print("Нет товаров, соответствующих условиям.")

############################################################################################################################################
mode = "r"
encoding = "utf-8"


def run_quiz():
    with open("questions.txt", mode=mode, encoding=encoding) as question_file, \
            open("answers.txt", mode=mode, encoding=encoding) as answers_file:
        questions = question_file.readlines()
        answers = answers_file.readlines()
    score = 0

    for i in range(len(questions)):
        question = questions[i].strip()
        correct_answer = answers[i].strip().lower()

        user_answer = input(f"{question}").strip().lower()

        if user_answer == correct_answer:
            print("ПРАВИЛЬНО!\n")
            score += 1
        else:
            print(f"НЕПРАВИЛЬНО! ПРАВИЛЬНЫЙ ОТВЕТ: {correct_answer}\n")
    print(f"Вы ответили правильно на {score} из {len(questions)} вопросов.")


run_quiz()

#####################################################################################################################################

import json

# Создание словаря
data = {
    "people": [
        {"name": "ALI", "age": 25},
        {"name": "OLGA", "age": 30},
        {"name": "IVAN", "age": 22},
        {"name": "MARIA", "age": 28},
        {"name": "SERGEY", "age": 35}
    ]
}

with open("people.json", "w") as json.file:
    json.dump(data, json.file, indent=4)

##############################################################################################################################################

import json
import csv

# Указываем кодировку
encoding = "utf-8"

# Чтение JSON данных из файла
with open("people.json", "r", encoding=encoding) as file:
    data = json.load(file)

# Запись данных в CSV файл
with open("people.csv", "w", encoding=encoding, newline="") as file:
    writer = csv.writer(file, delimiter=';')
    # Записываем заголовки
    writer.writerow(["person_id", "name", "age"])  # Заголовки CSV файла

    # Обрабатываем каждый элемент списка people
    for index, person in enumerate(data.get("people", []), start=1):
        try:
            name = person["name"]
            age = person["age"]
            writer.writerow([f"person{index}", name, age])
        except KeyError as e:
            print(f"Ошибка в структуре данных: отсутствует ключ {e}")

print("Данные успешно записаны в people.csv")
