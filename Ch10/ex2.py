class Car:
    def __init__(self,year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_car(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
        
    def get_speed(self):
        return self.__speed

user_car_year = input("Введите год изготовления авто:\n")
user_car_make = input("Введите производителя авто:\n")

save_car = Car(user_car_year, user_car_make)

for x in range(5):
    save_car.accelerate()
    print(f'Текущая скорость - {save_car.get_speed()}')

for x in range(5):
    save_car.break_car()
    print(f'Текущая скорость - {save_car.get_speed()}')