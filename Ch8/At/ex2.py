mystring = "привет пока попа рак"
count = 0
for ch in mystring:
    if ch == ' ':
        count +=1
print (f'Пробел повторяется {count} раз(а)')
