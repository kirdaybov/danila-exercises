class Patient:
    def __init__(self, name, adres, telnum, emergency_communication):
        self.__name = name
        self.__adres = adres
        self.__telnum = telnum
        self.__emergency_communication = emergency_communication

    def set_name(self, name):
        self.__name = name

    def set_adres(self, adres):
        self.__adres = adres

    def set_telnum(self, telnum):
        self.__telnum = telnum

    def set_emergency_communication(self, emergency_communication):
        self.__emergency_communication = emergency_communication

    def get_name(self):
        return self.__name 

    def get_adres(self):
        return self.__adres 

    def get_telnum(self):
        return self.__telnum

    def get_emergency_communication(self):
        return self.__emergency_communication

class Procedure:
    def __init__(self, procedure_name, procedure_date, doctor, price):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__doctor = doctor
        self.__price = price

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_price(self, price):
        self.__price = price

    def get_procedure_name(self):
        return self.__procedure_name   

    def get_procedure_date(self):
        return self.__procedure_date

    def get_doctor(self):
        return self.__doctor

    def get_price(self):
        return self.__price

patient_1 = Patient("Генадий Григорьевич Жопин","Юзорская обл., Г.Багов, 111666","8-800-555-3555","8-900-735-4999")

procedure_1 = Procedure("Врачебный осмотр","сегодняшняя","Ирвин","250.00")
procedure_2 = Procedure("Рентгенография","сегодняшняя","Джемисон","500.00")
procedure_3 = Procedure("Анализ крови","сегодняшняя","Смит","200.00")

total_price = float(procedure_1.get_price()) + float(procedure_2.get_price()) + float(procedure_3.get_price())

print('Информация о пациенте:')
print(f'Имя пациента: {patient_1.get_name()}')
print(f'Адрес пациента: {patient_1.get_adres()}')
print(f'Телефон пациента: {patient_1.get_telnum()}')
print(f'Телефон для эктренной связи: {patient_1.get_emergency_communication()}')
print()
print('Cведения о процедуре №1:')
print(f'Название процедуры: {procedure_1.get_procedure_name()}')
print(f'Дата процедуры: {procedure_1.get_procedure_date()}')
print(f'Врач процедуры: {procedure_1.get_doctor()}')
print(f'Стоимость процедуры: {procedure_1.get_price()}')
print()
print('Cведения о процедуре №2:')
print(f'Название процедуры: {procedure_2.get_procedure_name()}')
print(f'Дата процедуры: {procedure_2.get_procedure_date()}')
print(f'Врач процедуры: {procedure_2.get_doctor()}')
print(f'Стоимость процедуры: {procedure_2.get_price()}')
print()
print('Cведения о процедуре №3:')
print(f'Название процедуры: {procedure_3.get_procedure_name()}')
print(f'Дата процедуры: {procedure_3.get_procedure_date()}')
print(f'Врач процедуры: {procedure_3.get_doctor()}')
print(f'Стоимость процедуры: {procedure_3.get_price()}')
print()
print(f"Общая стоимость всех процедур - {total_price}")
