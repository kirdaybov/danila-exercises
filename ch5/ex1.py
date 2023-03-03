def km_to_miles_converter(killometres):
    miles = killometres * 0.6214
    print(f'{killometres} км = {miles:.2f} миль') 

killometres = float(input('Введите кол-во КМ:\n'))

km_to_miles_converter(killometres)