error = 0

for x in range(1,6):
    question = int(input(f'Введите кол-во ошибок за день\n'))
    eror = error + question
    print(f'За {x} день {error} ошибок')
print(f'Всего ошибок за пять дней - {error}')