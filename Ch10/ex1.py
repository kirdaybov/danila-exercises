class Pet:
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

name_pet = input('Введите имя питомца:\n')
animal_type_pet = input('Введите тип питомца:\n')
age_pet = input('Введите возраст питомца:\n')

savings_pet = Pet(name_pet,animal_type_pet,age_pet)

print(f'Имя Вашего питомца - {savings_pet.get_name()}')
print(f'Тип Вашего питомца - {savings_pet.get_animal_type()}')
print(f'Возраст Вашего питомца - {savings_pet.get_age()}')