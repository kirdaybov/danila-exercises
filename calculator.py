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
sum = 0
costume_enter = input(f'Здравствуйте!\nВы перевозили костюмы?\nВарианты ответа:Y/N\n')

if costume_enter.upper() == 'Y':
    costume_enter_count = input(f'Напишите количество\n')
    while not costume_enter_count.isnumeric():
        costume_enter_count = input('Напишите всё же число\n')
    costume_count = int(costume_enter_count)
    if 0 < costume_count <= 8:
        print('За костюмы Вы получите 600 руб.')
        sum += 600
    elif costume_count <= 13:
        print('За костюмы Вы получите 800 руб.')
        sum += 800
    elif costume_count <= 18:
        print('За костюмы Вы получите 1000 руб.')
        sum += 1000
    else:
        print('За костюмы Вы получите 1300 руб.')
        sum += 1300
enter = input(f'На данный момент у Вас {sum}руб.\nХотите ли Вы добавить что-то ещё?\nВарианты ответа:Y/N\n')
    
while enter.upper() == 'Y':
    entered_type = input('Введите что-то из:{}?\n'.format(product_type.keys()))
    if  entered_type.lower() in product_type.keys():
        entered_type_count = input(f'Напишите количество\n')
        while not entered_type_count.isnumeric():           
            entered_type_count = input('Напишите всё же число\n')
        cost = int(entered_type_count) * product_type[entered_type]
        sum += cost
        print(f'За {entered_type_count} {entered_type} Вы получите {cost}') 
    enter = input(f'На данный момент у Вас {sum}руб.\nХотите ли Вы добавить что-то ещё?\nВарианты ответа:Y/N\n')
print (f'Вы получите {sum}')

#разобраться, как питон работает с файлами.


#Условие - это тру или фолс. Действие - это действие.
#Int - От integer(Целочисленный)
#git add .==> git commit -m """ ==> git push.