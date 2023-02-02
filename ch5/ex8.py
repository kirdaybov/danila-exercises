area = int(input('Введите площадь окращеваемой поверхности:\n'))
paint_jar_price = int(input('Введите стоимость 5-ти литровой банки краски:\n'))
def calculate_paint_jar(area):
    VOLUME_JAR = 5.0
    number_of_jar_paint = (area // 10 * VOLUME_JAR) // VOLUME_JAR
    print (f'Вам понадобится - {number_of_jar_paint} банок краски')
    return number_of_jar_paint

def calculate_working_hours(area):
    WORKING_HOURS_PER_1_HOURS = 8 / 10
    time = area * WORKING_HOURS_PER_1_HOURS
    print(f'{time} - часов потребуется на работу')
    return time

def calculate_cost_of_work(time):
    WORK = 2000
    cost_of_work = WORK * time
    print(f'Стомость работы - {cost_of_work}')
    return cost_of_work

def calculate_cost_paint(paint_jar_price,amount_paint):
    cost_paint = paint_jar_price * amount_paint
    print(f'Стоимость затраченной краски - {cost_paint}')
    return cost_paint

def calculate_cost_work(cost_of_work, cost_of_paint):
    cost_work = cost_of_work + cost_of_paint
    print(f'Стоимость малярных работ - {cost_work}')

amount_paint = calculate_paint_jar(area)
time = calculate_working_hours(area)
cost_of_work = calculate_cost_of_work(time)
cost_of_paint = calculate_cost_paint(paint_jar_price, amount_paint)
calculate_cost_work(cost_of_work, cost_of_paint)

