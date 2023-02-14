line = input('Введите строку:\n')

symbol_frequencies = [0] * 2048

for symbol in line:
    index = ord(symbol)
    symbol_frequencies[index] += 1

index_most_frequent_symbol = 0
count_most_frequent_symbol = 0

for index in range(2048):
    if symbol_frequencies[index] > count_most_frequent_symbol:
       index_most_frequent_symbol = index
       count_most_frequent_symbol = symbol_frequencies[index]

print(f'Частота этого символа - {symbol_frequencies[index_most_frequent_symbol]}')
print(f'Самый частый символ - {chr(index_most_frequent_symbol)}')

    
    







