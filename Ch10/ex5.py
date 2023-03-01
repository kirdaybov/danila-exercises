class RetailItem:
    def __init__(self, description, amount, price):
        self.__description = description
        self.__amount = amount
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_amount(self, amount):
        self.__amount = amount

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description 

    def get_amount(self):
       return int(self.__amount)

    def get_price(self):
        return float(self.__price)

product_1 = RetailItem('Пиджак','12','59.95')
product_2 = RetailItem('Дизайнерские джинсы','40','34.95')
product_3 = RetailItem('Рубашка','20','24.95')   

