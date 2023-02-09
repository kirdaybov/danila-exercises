mystring = "прИвет ПОКА пОпА рАк"
count = 0
for ch in mystring:
    if ch.isupper():
        count +=1
print (f'БОЛЬШИЕ СИМВОЛЫ повторяется {count} раз(а)')