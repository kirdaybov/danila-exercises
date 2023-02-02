total_sales = int(input('Введите общий обьем продаж за месяц:\n'))

def colculate_council_tax(sales):
    council_tax = sales * 0.025
    print(f'Сумма муниципиального налога - {council_tax}')
    return council_tax

def colculate_federal_tax(sales):
    federal_tax = sales * 0.05
    print(f'Сумма федерального налога - {federal_tax}')
    return federal_tax

def colculate_total_tax(num1, num2):
    print(f'Общий налог с продаж - {num1 + num2}')

council_tax = colculate_council_tax(total_sales)
federal_tax = colculate_federal_tax(total_sales)
colculate_total_tax(council_tax, federal_tax)