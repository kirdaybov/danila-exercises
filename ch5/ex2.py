product = int(input('Введите величину покупки - '))

def count_federal_tax(product):
    federal_tax = product * 0.05
    print('Федеральный налог равен - ', federal_tax)
    return federal_tax
    
def count_regional_tax(product):
    regional_tax = product * 0.025
    print('Региональный налог равен - ', regional_tax)
    return regional_tax

def count_general_tax(tax1,tax2):
    print('Общий налог с продажи - ', tax1 + tax2)
    return tax1 + tax2

def count_grand_total(product, general_tax):
    print("Общая сумма продажи - ", product - general_tax)
    return product - general_tax

federal_tax = count_federal_tax(product)
regional_tax = count_regional_tax(product)
general_tax = count_general_tax(federal_tax, regional_tax)
count_grand_total(product, general_tax)



    