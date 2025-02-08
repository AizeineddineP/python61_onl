# первое задание на класс и его объекты!
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display_variables(self):
        print(f"Переменная 1: {self.var1}")
        print(f"Переменная 2: {self.var2}")

    def change_variables(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_of_variables(self):
        return self.var1 + self.var2

    def max_of_variables(self):
        return max(self.var1, self.var2)


# создать пример
sample = MyClass(10, 20)

# показать его на экран
sample.display_variables()

# Изменение переменных
sample.change_variables(15, 25)
sample.display_variables()

# сумма переменных
print(f"Сумма переменных: {sample.sum_of_variables()}")

# Нахождение наибольшего значения
print(f"Наибольшее значение: {sample.max_of_variables()}")


############################################################################################################################################

# второе задание

class Counter:
    def __init__(self, min_value=0, max_value=10, current_value=None):
        if min_value > max_value:
            raise ValueError("Минимальное значение не может быть больше максимального.")
        self.min_value = min_value
        self.max_value = max_value
        if current_value is None:
            self.current_value = min_value
        elif min_value <= current_value <= max_value:
            self.current_value = current_value
        else:
            raise ValueError("Текущее значение должно быть в пределах диапазона.")

    def increment(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            return True  # Успешное увеличение
        return False  # Достигнут максимум

    def decrement(self):
        if self.current_value > self.min_value:
            self.current_value -= 1
            return True  # Успешное уменьшение
        return False  # Достигнут минимум

    @property
    def value(self):
        return self.current_value

    def reset(self):
        self.current_value = self.min_value


# Демонстрация
if __name__ == "__main__":
    counter = Counter(min_value=0, max_value=5, current_value=2)
    print("Текущее значение:", counter.value)
    while counter.increment():
        print("Увеличено:", counter.value)
    print("Достигнут максимум.")


############################################################################################################################################

# 3e задание

class Shop:
    def __init__(self):
        # Инициализация пустого списка для хранения продуктов
        self.products = []

    # Добавляет продукт в магазин.
    def add_product(self, name, price, quantity=1):
        # Проверяем, существует ли продукт с таким названием
        for product in self.products:
            if product['name'] == name:
                # Если продукт уже есть, увеличиваем его количество
                product['quantity'] += quantity
                print(
                    f"Количество продукта '{name}' увеличено на {quantity}. Текущее количество: {product['quantity']}")
                return
        # Если продукта нет, добавляем его в список
        self.products.append({'name': name, 'price': price, 'quantity': quantity})
        print(f"Продукт '{name}' добавлен в магазин.")

    # Удаляет продукт из магазина или уменьшает его количество.
    def remove_product(self, name, quantity=1):
        for product in self.products:
            if product['name'] == name:
                if product['quantity'] > quantity:
                    # Если количество больше, чем нужно удалить, уменьшаем количество
                    product['quantity'] -= quantity
                    print(
                        f"Количество продукта '{name}' уменьшено на {quantity}. Текущее количество: {product['quantity']}")
                else:
                    # Если количество меньше или равно, удаляем продукт полностью
                    self.products.remove(product)
                    print(f"Продукт '{name}' удален из магазина.")
                return
        print(f"Продукт '{name}' не найден в магазине.")

    # Ищет продукт по названию.
    def find_product(self, name):
        for product in self.products:
            if product['name'] == name:
                return product
        return None

    # Выводит список всех продуктов в магазине.
    def list_products(self):
        if not self.products:
            print("В магазине нет продуктов.")
        else:
            print("Список продуктов в магазине:")
            for product in self.products:
                print(f"Название: {product['name']}, Цена: {product['price']}, Количество: {product['quantity']}")


# Демонстрация работы класса
if __name__ == "__main__":
    # Создаем магазин
    shop = Shop()

    # Добавляем продукты
    shop.add_product("Яблоки", 50, 10)
    shop.add_product("Бананы", 30, 5)
    shop.add_product("Молоко", 80, 2)

    # Выводим список продуктов
    shop.list_products()

    # Ищем продукт
    product = shop.find_product("Бананы")
    if product:
        print(f"Найден продукт: {product['name']}, Цена: {product['price']}, Количество: {product['quantity']}")
    else:
        print("Продукт не найден.")

    # Удаляем продукт
    shop.remove_product("Яблоки", 5)
    shop.remove_product("Молоко")

    # Выводим обновленный список продуктов
    shop.list_products()


############################################################################################################################################

# 4e задание

class MoneyBox:
    def __init__(self, capacity):
        """
        Конструктор копилки.
        :param capacity: Вместимость копилки (максимальное количество монет).
        """
        self.capacity = capacity  # Вместимость копилки
        self.coins = 0  # Текущее количество монет в копилке

    def can_add(self, v):
        """
        Проверяет, можно ли добавить v монет в копилку.
        :param v: Количество монет, которое нужно добавить.
        :return: True, если можно добавить v монет, иначе False.
        """
        return self.coins + v <= self.capacity

    def add(self, v):
        """
        Добавляет v монет в копилку.
        :param v: Количество монет, которое нужно добавить.
        """
        if self.can_add(v):
            self.coins += v
            print(f"Добавлено {v} монет. Текущее количество монет: {self.coins}")
        else:
            print(f"Невозможно добавить {v} монет: превышена вместимость копилки.")


# Демонстрация работы класса
if __name__ == "__main__":
    # Создаем копилку с вместимостью 10 монет
    money_box = MoneyBox(10)

    # Пытаемся добавить монеты
    money_box.add(5)  # Добавляем 5 монет
    money_box.add(4)  # Добавляем 4 монеты
    money_box.add(2)  # Пытаемся добавить 2 монеты (не получится, так как превысит вместимость)

    # Проверяем, можно ли добавить ещё монеты
    print("Можно ли добавить 3 монеты?", money_box.can_add(3))  # False
    print("Можно ли добавить 1 монету?", money_box.can_add(1))  # True
