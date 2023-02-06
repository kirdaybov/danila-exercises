name = input("Введите своё имя:\n")
description = input("Опишите себя:\n")

file_HTML = open('User description.HTML', 'w')

file_HTML.write(f'{name}\n')
file_HTML.write(description)

file_HTML.close()
print('Данные записаны в файл "User description.HTML"')