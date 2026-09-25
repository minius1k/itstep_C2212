class Engine:
    def __init__(self, fuel_type, power):
        self.fuel_type = fuel_type
        self.power = power

    def start_engine(self):
        print(f"Двигун ({self.fuel_type}, {self.power} к.с.) запущено!")


class Electronics:
    def __init__(self, screen_size, has_gps):
        self.screen_size = screen_size
        self.has_gps = has_gps

    def show_navigation(self):
        if self.has_gps:
            print(f"Навігація працює на екрані {self.screen_size} дюймів.")
        else:
            print("GPS відсутній.")


class SmartCar(Engine, Electronics):
    def __init__(self, brand, fuel_type, power, screen_size, has_gps):
        Engine.__init__(self, fuel_type, power)
        Electronics.__init__(self, screen_size, has_gps)
        self.brand = brand

    def drive(self):
        print(f"Автомобіль {self.brand} готовий до їзди:")
        self.start_engine()
        self.show_navigation()


car = SmartCar("BMW", "бензин", 250, 12, True)
car.drive()