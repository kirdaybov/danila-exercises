mystring = "1 9 1 ра57к"
count = 0
for ch in mystring:
    if ch.isdigit():
        count +=1
print (f'Числа повторяется {count} раз(а)')