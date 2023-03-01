from ex5 import RetailItem

class CashRegister:
    def __init__(self):
        self.__product = []

    def clear_shopping_cart(self):
        self.__product = []

    def purchase_item(self, retail_item):
        self.__product.append(retail_item)
        print('Товар добавлен в список')

    def get_total(self):
        total = 0.0
        for product in self.__product:
            total += product.get_price() 
        
        return total
       
    def show_items(self):
        print('Товары в корзине')
        print()
        for product in self.__product:
            print(product)
            print()

def get_user_choice():
    print('MЕНЮ')
    print('---------------------------------')
    print('1. Штаны')
    print('2. Майка')
    print('3. Куртка')
    print('4. Носки')
    print('5. Платье')
    print()

    choice = int(input('Введите номер товара, который Вы хотите приобрести\n'))

    while choice > DRESS or choice < PANTS:
        choice = int(input('Введите допустимый номер товара:\n'))

    return choice

PANTS = 1
T_SHIRT = 2
JACKET = 3
SOCKS = 4
DRESS = 5

pants = RetailItem('Штаны','5','72.90')
t_shirt = RetailItem('Майка','15','20.95')
jacket = RetailItem('Куртка','9','112.95')
socks = RetailItem('Носки','21','12.95')
dress = RetailItem('Платье','3','78.95')

sale_product = {PANTS: pants, T_SHIRT: t_shirt, JACKET: jacket, SOCKS: socks, DRESS: dress}

shopping_basket = CashRegister()

flag = "Y"

while flag.upper() == "Y":
    user_choice = get_user_choice()
    product = sale_product[user_choice]
    if product.get_amount() == 0:
        print('Товар закончился')
    else:
        shopping_basket.purchase_item(product)

        new_amount_product = RetailItem(product.get_description(), product.get_amount() - 1, product.get_price())
        sale_product[user_choice] = new_amount_product

        flag = input('Вы хотите ещё что-то купить? Если "нет" - нажмите любой символ, если "да" - нажмите "Y\n')


print(f'Cумма Вашей покупки составляет: {shopping_basket.get_total():.2f}')
shopping_basket.show_items()
shopping_basket.clear_shopping_cart()