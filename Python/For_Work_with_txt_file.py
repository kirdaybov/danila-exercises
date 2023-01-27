#Запись в текстовый файл
with open("For_lessons_with_text_python.txt", 'w') as file:
    file.write('А это я написал из питона')
#это правит сразу весь файл.

with open("For_lessons_with_text_python.txt", "a") as file:
    file.write("\nа это уже 'дописал из питона'")
#это дописывает в файл

with open("For_lessons_with_text_python.txt", "r") as file:
    for line in file:
        print(line, end="")
#выводит в консоли, что в файле

FILENAME = "For_lessons_with_text_python.txt"
# определяем пустой список
messages = list()
 
for i in range(4):
    message = input("\nВведите строку " + str(i+1) + ": ")
    messages.append(message + "\n")
 
# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)
 
# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")

#Найти функция, которая возвращает список по пробелам