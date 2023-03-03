line = 'ОстановисьИПочувствуйЗапахРоз'

new_line = line[0]

for symbol in line[1:]:
    if symbol.isupper():
        new_line += " " + symbol.lower()
    else:
        new_line += symbol

print(new_line)        

