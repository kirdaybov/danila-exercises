
class Car:
    def __init__(self, num_of_wheels, year_of_making, diesel_engine, brand, color):
        self.num_of_wheels = num_of_wheels
        self.diesel_engine = diesel_engine
        self.year_of_making = year_of_making
        self.brand = brand
        self.color = color

    def print_car(self):
        print("Car info: ")
        print(self.num_of_wheels)
        print(self.diesel_engine)
        print(self.year_of_making)
        print(self.brand)
        print(self.color)

#car1 = Car(4, True, 'Renault', 'Red')
car1_wheels = 4
car1_diesel_engine = True
car1_brand = 'Renault'
car1_color = 'Red'

#car2 = Car(3, True, 'Opel', 'Yellow')
car2_wheels = 3
car2_diesel_engine = True
car2_brand = 'Opel'
car2_color = 'Yellow'

#car3 = Car(8, False, 'Kamaz', 'White')
car3_wheels = 8
car3_diesel_engine = False
car3_brand = 'Kamaz'
car3_color = 'White'

# 0 - num of wheels, 1 - diesel or not, 2 - year of making 3 - brand, 4 - color
car1 = [4, True, 1998, 'Renault', 'Red']
car2 = [3, True, 1998, 'Opel', 'Yellow']
car3 = [8, False, 2005, 'Kamaz', 'White']

index = 0
cars = [car1, car2, car3]












while index < len(cars):
    print(cars[index][2])
    index = index + 1





while index < len(cars):
    print(cars[index].brand)
    cars[index].print_car()
    index = index + 1