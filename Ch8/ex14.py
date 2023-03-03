infile = open('GasPrices.txt', 'r')

GasPrices = infile.readline()

infile.close()

GasPrices = GasPrices.split('-')
GasPrices = GasPrices[2].split(':')

print(GasPrices)

#решаем с Кириллом