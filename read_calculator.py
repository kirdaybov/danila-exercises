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

#1. читать файл циклом по строкам
#2. на каждой итерации разделить строку на список слов
#3. первое слово в списке - ключ для словаря, по нему получаем цену
#4. второе слово в списке - количество, преобразовываем его в инт
#5. перемножаем количество и цену получаем профит

sum = 0

def in_dictionary(type, amount):
  if not (type in product_type.keys()):
    print("Ошибка, в строке на первом месте слово не из словаря. Проверьте текстовый документ")
    return 0
  if not amount.isnumeric():
    print('Ошибка, в строке на втором месте не число. Проверьте текстовый документ')
    return 0
  entered_type = type
  amount1 = int(amount)
  enter_type_price = product_type[entered_type]
  cost = amount1 * enter_type_price
  print (f'Вы получите {cost}')
  return cost
  
def costume_cost(costume_txt, amount_costume):
  costume_txt = words[0]
  amount_costume = words[1] 
  cost = 0
  if 'costume' == costume_txt:
    costume_count = int(amount_costume)
    if 0 < costume_count <= 8:
        print('За костюмы Вы получите 600 руб.')
        cost += 600
        return cost
    elif costume_count <= 13:
        print('За костюмы Вы получите 800 руб.')
        cost += 800
        return cost
    elif costume_count <= 18:
        print('За костюмы Вы получите 1000 руб.')
        cost += 1000
        return cost
    else:
        print('За костюмы Вы получите 1300 руб.')
        cost += 1300
        return cost

with open("rc.txt", "r") as file1:
    for line in file1:
        words = line.split()
        if len(words) == 2:
          if 'costume' == words[0]:
            sum += costume_cost(words[0], words[1])
          else:
            sum += in_dictionary(words[0], words[1])
print(f'Всего Вы получите {sum}') 


        
      
        


#прочитать, что такое объект
#прочитать, что такое lambda
#прочитать, что такое стек и куча(stack, heap)
#git add .==> git commit -m """ ==> git push.
  

  
  
 



