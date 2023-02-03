def calculate_kinetic_energy(mass, speed):
    kinetic_energy = 1 / 2 * mass * speed ** 2
    print (f'Кинетическая энергия равна - {kinetic_energy}')
    return kinetic_energy

mass = float(input('Введите значение массы в КГ:\n'))
speed = float(input('Введите скорость в М\С:\n'))

calculate_kinetic_energy(mass,speed)
