class Person:
    def __init__(self, name, adress, telnum):
        self.__name = name
        self.__adress = adress
        self.__telnum = telnum

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_telnum(self, telnum):
        self.__telnum = telnum

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_telnum(self):
        return self.__telnum

    def __str__(self):
        result = 'Имя: ' + self.get_name() + '\n' + \
                 'Адресс: ' + self.get_adress() + '\n' + \
                 'Телефонный номер: ' + self.get_telnum() 
        return result

class Customer(Person):
    def __init__(self, name, adress, telnum, mailing_list):
        Person.__init__(self, name, adress, telnum)
        self.__mailing_list = mailing_list

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_mailing_list(self):
        return self.__mailing_list

name = input('Введите имя:\n')
adress = input('Введите адресс:\n')
telnum = input('Введите телефон:\n')
in_mailing_list = input('Клиент хочет быть в списке рассылки?\nЕсли "Да", введите "Y". Если "Нет", введите "N":\n')

if in_mailing_list.upper() == 'Y':
    in_mailing_list = True
else:
    in_mailing_list = False

client = Customer(name, adress, telnum, in_mailing_list)

print('Инормация о клиенте:\n')
print(client)    
