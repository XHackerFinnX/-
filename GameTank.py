import random
import time


class Tank():

    def __init__(self, model, armor, damage, health):
        self.model = model
        self.armor = armor
        self.damage = damage
        self.health = health

    def print_info(self):
        print(f"{self.model} имеет лобовую броню {self.armor} мм.\nПри {self.health} ед. здоровья и урон в {self.damage} единиц. \n")
        if sum_damage != []:
            print(
                f"Слабое попадание {min(sum_damage)}. Сильное попадание {(max(sum_damage))}")

    def shot(self):
        if obj2.health <= 0:
            print(f"Экипаж танка {obj2.model} уничтожен! \n")
        else:
            print(
                f"{self.model}: Точно в цель, у противника {obj2.model} осталось {obj2.health} единиц здоровья! \n")

    def health_down(self):
        if self.health >= 0:
            print(
                f"{obj2.model}: Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья! \n")
        else:
            print(f"Экипаж танка {self.model} уничтожен! \n")


class Tank_enemy():

    def __init__(self, model, armor, damage, health):
        self.model = model
        self.armor = armor
        self.damage = damage
        self.health = health


obj1 = Tank(input("Введите модель танка: "), int(input("Введите броню танка: ")),
            random.randint(100, 500), int(input("Введите здоровье танка: ")))

obj2 = Tank_enemy("Tiger I", 50, random.randint(100, 500), 100)

sum_damage = []

while True:
    if (obj2.health > 0) and (obj1.health > 0):
        fire = input(
            'Нажмите "+" чтобы выстрелить в танк Tiger I \nНажмите "i" чтобы посмотреть информацию о своем танке \n')
        if fire == "+":
            obj2.health = obj2.health - (obj1.damage // obj2.armor)
            obj1.shot()
            sum_damage.append(obj1.damage)
            obj1.damage = random.randint(100, 500)
            if obj2.health <= 0:
                False
            else:
                print(f"Теперь стреляет {obj2.model}")
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.\n')
                time.sleep(1)

                obj1.health = obj1.health - (obj2.damage // obj1.armor)
                obj1.health_down()
                obj2.damage = random.randint(100, 500)
        else:
            obj1.print_info()
    if obj1.health <= 0:
        False
    else:
        False
