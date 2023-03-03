class Information:
    def __init__(self, name, adres, age, telnum):
        self.__name = name
        self.__adres = adres
        self.__age = age
        self.__telnum = telnum
        
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_adres(self, adres):
        self.__adres = adres

    def set_telnum(self, telnum):
        self.__telnum = telnum

    def get_name(self):
        return self.__name 

    def get_age(self):
       return self.__age 

    def get_adres(self):
        return self.__adres 

    def get_telnum(self):
        return self.__telnum

human_list = []

print("Введите данные о людях")
for x in range(1,4):
    print(f'Введите данные человека № {x}')
    name = input('Введите имя:\n')
    adres = input('Введите адресс:\n')
    age = input('Введите возраст:\n')
    telnum = input('Введите сотовый номер:\n')
    print()

    human = Information(name, adres, age, telnum)
    human_list.append(human)

for item in human_list:
    print(item.get_name())
    print(item.get_age())
    print(item.get_adres())
    print(item.get_telnum())
    print()


