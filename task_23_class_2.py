class BankAccount:
    def __init__(self, balance: float = 0.0):
        self.__balance = balance
        self.daily_limit = 5000.0
        self.withdrawals_today = 0
        self.max_withdrawals = 3

    def deposit(self, amount: float):
        """
        Добавляет деньги на счет. Только положительные суммы принимаются.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Баланс успешно пополнен на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount: float):
        """
        Снимает деньги со счета, если:
        1. Сумма запроса не превышает дневной лимит.
        2. У пользователя есть доступные попытки снятия.
        3. На счете достаточно средств.
        """
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return

        if self.withdrawals_today >= self.max_withdrawals:
            print("Превышено количество доступных снятий за сегодня.")
            return

        if amount > self.daily_limit:
            print(f"Сумма превышает дневной лимит в {self.daily_limit}.")
            return

        if amount > self.__balance:
            print("Недостаточно средств на счете.")
            return

        # Успешное снятие
        self.__balance -= amount
        self.withdrawals_today += 1
        print(f"Успешно снято {amount}. Остаток на счете: {self.__balance}")

    def get_balance(self):
        """
        Возвращает текущий баланс.
        """
        print(f"Текущий баланс: {self.__balance}")


account = BankAccount(balance=10000)
account.deposit(2000)
account.deposit(2000)
account.deposit(2000)
account.deposit(2000)
account.deposit(2000)
account.withdraw(5000)
account.withdraw(4000)
account.withdraw(400)
account.withdraw(4000)
account.get_balance()


#####################################################################################################################
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hunger = 100  # 100 - сыт, 0 - голоден

    def make_sound(self):
        pass

    def eat(self):
        self.hunger = 100
        print(f"{self.name} поел и теперь сыт!")

    def get_hungry(self):
        """
        Уровень голода уменьшается на 10.
        """
        if self.hunger > 0:
            self.hunger -= 10
            print(f"{self.name} проголодался. Уровень сытости: {self.hunger}")
        else:
            print(f"{self.name} очень голоден!")

    def is_hungry(self):
        """
        Проверка, сыт ли животное.
        """
        return self.hunger <= 50


class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} рычит: Ррррр!")

    def hunt(self):
        if self.hunger <= 30:
            print(f"{self.name} пошел на охоту!")
            self.eat()  # После удачной охоты лев ест
        else:
            print(f"{self.name} сыт, охота пока не нужна.")


class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} трубит: Тууууу!")

    def trumpet(self):
        print(f"{self.name} издает громкий звук: Тууууу!")


class Penguin(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук: Кря-кря!")

    def swim(self):
        print(f"{self.name} плавает в воде!")
        self.get_hungry()  # Плавание делает пингвина голодным


# Создаем список животных
animals = [
    Lion("Симба", 5),
    Elephant("Дамбо", 10),
    Penguin("Пингви", 3)
]

# Все животные издают звук
for animal in animals:
    animal.make_sound()

print("\nКормление животных...")
for animal in animals:
    if animal.is_hungry():
        animal.eat()
    else:
        print(f"{animal.name} пока не голоден.")

print("\nСпецифические действия животных...")
animals[0].hunt()  # Лев охотится
animals[1].trumpet()  # Слон трубит
animals[2].swim()  # Пингвин плавает


#######################################################################################################################

class Temperature:
    def __init__(self, celsius: float):
        # Устанавливаем температуру, проверяя нижнюю границу
        if celsius < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C!")
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Возвращает температуру в Цельсиях."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """Позволяет изменять температуру, проверяя, чтобы она не была ниже -273.15°C."""
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Возвращает температуру в Фаренгейтах."""
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        """Возвращает температуру в Кельвинах."""
        return self._celsius + 273.15


# Создаем новый объект класса Temperature
temp = Temperature(25)

print(f"Температура в Цельсиях: {temp.celsius}°C")  # 25°C
print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")  # 77.0°F
print(f"Температура в Кельвинах: {temp.kelvin}K")  # 298.15K

# Меняем температуру
temp.celsius = -50
print(f"\nНовая температура в Цельсиях: {temp.celsius}°C")  # -50°C
print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")  # -58.0°F
print(f"Температура в Кельвинах: {temp.kelvin}K")  # 223.15K

# Попытка установить температуру ниже -273.15
try:
    temp.celsius = -300  # Ошибка: Температура ниже абсолютного нуля
except ValueError as e:
    print(f"\nОшибка: {e}")
