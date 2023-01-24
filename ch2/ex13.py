bed_length = float(input('Введите длину гряды в метрах\n'))
size_of_space_in_meters = float(input('Введите пространство, занимаемое концевой опорой в метрах\n'))
distance_between_grapes = float(input('Введите расстояние между виноградными лозами в метрах\n'))
number_of_vines = (bed_length - (2 * size_of_space_in_meters)) / distance_between_grapes
print('На гряде поместятся -', number_of_vines, 'лоз(а)')
