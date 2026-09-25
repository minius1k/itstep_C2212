class House:
    def __init__(self):
        self.food = 10
        self.money = 100

    def info(self):
        print(f"У будинку: їжі = {self.food}, гривень = {self.money}")


class Human:
    def __init__(self, name, house):
        self.name = name
        self.energy = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.energy += 20
            print(f"{self.name} поїв(ла). Енергія: {self.energy}")
        else:
            print(f"У будинку немає їжі для {self.name}!")

    def work(self):
        if self.energy >= 15:
            self.energy -= 15
            self.house.money += 50
            print(f"{self.name} попрацював(ла) і заробив(ла) 50 гривень. Енергія: {self.energy}")
        else:
            print(f"{self.name} занадто замучений(а), щоб працювати.")

    def buy_food(self):
        if self.house.money >= 30:
            self.house.money -= 30
            self.house.food += 30
            print(f"{self.name} купив(ла) їжу.")
        else:
            print("Не вистачає гривень на їжу!")

    def live_day(self):
        print(f"\n--- День {self.name} ---")
        if self.energy < 20:
            self.eat()
        elif self.house.food < 10:
            self.buy_food()
        else:
            self.work()


# Симуляція
my_house = House()
person = Human("Олексій", my_house)

for day in range(1, 4):
    print(f"\n=== ДЕНЬ {day} ===")
    my_house.info()
    person.live_day()