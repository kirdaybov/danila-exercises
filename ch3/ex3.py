age = int(input("Введите возраст: \n"))
if age <= 1:
    print("младенец")
elif 1 < age < 13:
    print("ребёнок")
elif 13 <= age < 20:
    print("подросток")
elif 20 <= age:
    print("взрослый")