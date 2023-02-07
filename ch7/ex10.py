infile = open('WorldSeriesWinners.txt', 'r')

winners = infile.readlines()

infile.close()

search = input('Введите название команды, которую нужно найти:\n')
years = 0

for x in winners:
    if x == search:
        years += 1

print(f'Команда побеждала {years}')