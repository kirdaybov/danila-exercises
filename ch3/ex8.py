people = int(input('Сколько участников пикника? \n'))
hot_dog = int(input('Сколько хот-догов одному человеку? \n'))
package_sosige = 10 #сосисок в пачке
package_broud = 8 #Булок в пачке
total_hot_dog = people * hot_dog # сколько нужно хот-догов и сосисок
total_hot_dog_broud = total_hot_dog * 2 #сколько нужно булок для хот-догов
print ('Всего нужно сосисок - ', total_hot_dog)
print('Всего нужно булок - ', total_hot_dog_broud)
if people >= 0 and total_hot_dog % package_sosige != 0: #если людей больше 0 и остаток от деления кол-во хот-догов на сосиски не равно 0 то:
    min_package_sosige = total_hot_dog // package_sosige + 1 # кол-во хот-догов делим на пачку сосисок и прибовляем одну, чтобы не закончилась в пачке
    remainder_sosige = min_package_sosige * package_sosige - total_hot_dog # минимальное количество пакетов сосисок умножаем на кол-во сосисок в них и вычитаем кол-во хот догов
else:
    min_package_sosige = total_hot_dog // package_sosige
    remainder_sosige = 0
print('Минимальное кол-во упаковок с сосисками - ' , min_package_sosige) 
print('Кол-во оставшихся сосисок - ' , remainder_sosige) 
if people >= 0 and total_hot_dog % package_broud != 0:
    min_package_broud = total_hot_dog_broud // package_broud + 1
    remainder_broud = min_package_broud * package_broud - total_hot_dog_broud
else:
    min_package_broud = total_hot_dog_broud // package_broud
    remainder_broud = 0
print('Минимальное кол-во упаковок с булками - ' , min_package_broud) 
print('Кол-во оставшихся булок - ' , remainder_broud) 
