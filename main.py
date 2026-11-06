class Car:
    def __init__(self, brand, model, engine, power, torque, max_speed, acceleration, body, year):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.power = power
        self.torque = torque
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.body = body
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})\n" \
               f"  - Кузов: {self.body}\n" \
               f"  - Двигун: {self.engine} (сток)\n" \
               f"  - Потужність: {self.power}\n" \
               f"  - Крутний момент: {self.torque}\n" \
               f"  - Максимальна швидкість: {self.max_speed}\n" \
               f"  - Розгін 0-100 км/год: {self.acceleration}"


class Catalog:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_cars(self):
        for index, car in enumerate(self.cars, start=1):
            print(f"{index}. {car.brand} {car.model}")

    def get_car(self, index):
        if 0 <= index < len(self.cars):
            return self.cars[index]
        return None


def main():
    catalog = Catalog()

    catalog.add_car(Car(
        brand="BMW",
        model="M4 Competition",
        engine="3.0L S58 Twin-Turbo I6",
        power="510 к.с. при 6250 об/хв",
        torque="650 Нм при 2750-5500 об/хв",
        max_speed="250 км/год (електронно обмежена, з пакетом M Driver's — 290 км/год)",
        acceleration="3.9 с",
        body="G82 Coupe",
        year="2021"
    ))

    catalog.add_car(Car(
        brand="Toyota",
        model="Mark II",
        engine="2.5L 1JZ-GTE Turbo I6",
        power="280 к.с. при 6200 об/хв (заводський ліміт)",
        torque="378 Нм при 2400 об/хв",
        max_speed="180 км/год (обмежена японським стандартом)",
        acceleration="6.1 с",
        body="JZX100 Sedan",
        year="1996"
    ))

    catalog.add_car(Car(
        brand="Mercedes-Benz",
        model="G63 AMG",
        engine="4.0L M177 Twin-Turbo V8",
        power="585 к.с. при 6000 об/хв",
        torque="850 Нм при 2500-3500 об/хв",
        max_speed="220 км/год (з пакетом AMG Driver's — 240 км/год)",
        acceleration="4.5 с",
        body="W463A SUV",
        year="2018"
    ))

    while True:
        print("\n=== КАТАЛОГ СПОРТИВНИХ АВТОМОБІЛІВ ===")
        print("1. Переглянути список авто")
        print("2. Вийти")

        choice = input("Оберіть варіант (1-2): ").strip()

        if choice == "1":
            while True:
                print("\n--- ДОСТУПНІ МОДЕЛІ ---")
                catalog.list_cars()
                print("0. Назад у головне меню")

                car_choice = input("Введіть номер авто (або 0 для повернення): ").strip()

                if car_choice == "0":
                    break
                elif car_choice.isdigit():
                    idx = int(car_choice) - 1
                    selected_car = catalog.get_car(idx)

                    if selected_car:
                        print("\n========================================")
                        print(selected_car.get_info())
                        print("========================================")
                        input("\nНатисніть Enter, щоб повернутися до списку...")
                    else:
                        print("Помилка: авто з таким номером немає в списку!")
                else:
                    print("Помилка: введіть число!")

        elif choice == "2":
            print("Вихід з програми...")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()