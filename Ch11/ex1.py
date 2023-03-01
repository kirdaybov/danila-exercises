class Employee:
    def __init__(self,name, ID):
        self.__name = name
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    def set_ID(self,ID):
        self.__ID = ID

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

class ProductionWorker(Employee):
    def __init__(self,name,ID,shift_number,bid): #bid - ставка
        Employee.__init__(self,name, ID)
        self.__shift_number = shift_number
        self.__bid = bid

    def set_shift_number(self,shift_number):
        self.__shift_number = int(shift_number)

    def set_bid(self, bid):
        self.__bid = float(bid)

    def get_shift_number(self):
        return self.__shift_number

    def get_bid(self):
        return self.__bid

    def __str__(self):
        result = 'Имя: ' + self.get_name() + '\n' + \
                 'ID: ' + self.get_ID() + '\n' + \
                 'Смена: ' + self.get_shift_number() + '\n' + \
                 'Ставка: ' + self.get_bid()
        return result

name = input('Введите имя сотрудника:\n')
id = input('Введите ID сотрудника:\n')
shift_number = input('Введите номер смены, где "1" - дневная, а "2" - вечерняя:\n')
if shift_number == '1':
    shift_number = 'Дневная'
elif shift_number == '2':
    shift_number = 'Вечерняя'
else:
    shift_number = shift_number
bid = input('Введите почасовую оплату труда:\n')

employee1 = ProductionWorker(name, id, shift_number, bid)

print('Информация о сотруднике:')
print(employee1)


        
        