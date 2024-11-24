class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Звук животного"

    def eat(self):
        return f"{self.name} ест."


# Реализация наследования

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "рыыыкк"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "шшшш"


# Демонстрация полиморфизма

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


# Пример использования

if __name__ == "__main__":
    parrot = Bird("Кеша", 2, "Средний")
    lion = Mammal("Лева", 5, "Золотистый")
    snake = Reptile("Ка", 3, "Гладкая")

    animals = [parrot, lion, snake]
    animal_sound(animals)

    def info(animals):
        for animal in animals:
            print(f"Имя: {animal.name}, Возраст: {animal.age}")

    info(animals)

# Использование композиции для создания класса Зоопарк

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} добавлен в зоопарк.")

    def add_staff_member(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} добавлен в персонал зоопарка.")


# Создание классов для сотрудников

class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Пример использования всех классов

if __name__ == "__main__":
    # Создание зоопарка
    zoo = Zoo()

    # Создание животных
    parrot = Bird("Попугай", 2, "Средний")
    lion = Mammal("Лев", 5, "Золотистый")
    snake = Reptile("Змея", 3,"Гладкая")

    # Добавление животных в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Создание сотрудников
    zooKeeper = ZooKeeper("Алиса", "Смотритель")
    veterinarian = Veterinarian("Боб", "Ветеринар")

    # Добавление сотрудников в зоопарк
    zoo.add_staff_member(zooKeeper)
    zoo.add_staff_member(veterinarian)

    # Действия сотрудников
    zooKeeper.feed_animal(lion)
    veterinarian.heal_animal(snake)