rectangle_width1 = int(input("Введите ширину прямоугольника 1: \n"))
rectangle_lengths1 = int(input("Введите длину прямоугольника 1: \n"))
rectangle_width2 = int(input("Введите ширину прямоугольника 2: \n"))
rectangle_lengths2 = int(input("Введите длину прямоугольника 2: \n"))
area_of_a_rectangle1 = rectangle_width1 * rectangle_lengths1
area_of_a_rectangle2 = rectangle_width2 * rectangle_lengths2
if area_of_a_rectangle1 > area_of_a_rectangle2:
    print("Площадь первого прямоугольника больше")
elif area_of_a_rectangle1 < area_of_a_rectangle1:
    print ("Площадь второго прямоугольника больше")
elif area_of_a_rectangle1 == area_of_a_rectangle2:
    print("Площадь прямоугольников равна")