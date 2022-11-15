#costume 
#Если костюмов до 8 = 600 руб
#9 - 14 = 800 руб
#14 - 19 = 1000 руб.
#>19 = 1300 руб.

product_type = {
  'box' : 50, 
  'loudspeakers' : 50,
  'head' : 50,
  'wings' : 50,
  'notebook' : 50,
  'carpet' : 50,
  'dive' : 50,
  'booom' : 50,
  'canister' : 50,
  'master_class' : 100,
  'big_costume' : 100,
  'big_loudspeakers' : 200,
  'requisite' : 0,
}
enter = input(f'Хотите ли Вы добавить что-то ещё?\nВарианты ответа:Y/N\n')

if enter.upper() == 'Y':
    entered_type = input('Введите что-то из:{}?\n'.format(product_type.keys()))
    if  entered_type.lower() in product_type.keys():
        entered_type_count = input(f'Напишите количество\n')
        while not entered_type_count.isnumeric():           
            entered_type_count = input('Напишите всё же число\n')
        cost = int(entered_type_count) * product_type[entered_type]
        print(f'За {entered_type_count} {entered_type} Вы получите {cost}') 

elif enter.upper() == 'N':
    print ('Всего доброго!')
else:
    print('Вы ввели не то( Надеюсь, что Вы хотели закрыть программу,\nв противном случае мы не оставили Вам выбора.')


#Зациклть эту программу и сделать выход из ней
#While - пока
#Условие - это тру или фолс. Действие - это действие.
#Int - От integer(Целочисленный)