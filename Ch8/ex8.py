line = input('Введите любое предложение:\n')

line = line.split() #преобразуем в список

line[0] = line[0].title() #Делаем первый символ в строке большим

for sumbol in range(len(line) - 1): #перебираем каждый символ в строке
    if line[sumbol][-1] == '.' or line[sumbol][-1] == '!' or line[sumbol][-1] == "?": #если последний символ в строке ".!?" то переходим к следующему элементу в списке, и делаем его первый символ заглавным
        line[sumbol + 1] = line[sumbol + 1].title()
line_str = " ".join(line) #функция join преобразовывает список в строку
print(line_str)

