def calculete_drop_height(time):
    distance = 1 / 2 * 9.8 * time ** 2
    print(f'За {time} тело пролетело {distance:.1f} метров')
    return distance

for x in range(1,11):
    calculete_drop_height(x)