steps_file = open('steps.txt', 'r')
count = 0
steps_in_january = 0
for line in range(1,32):
    steps_in_day = int(line)
    count += 1
    steps_in_january += steps_in_day
    
average_steps = steps_in_january // count
print(f'Среднее кол-во шагов за январь - {average_steps}')

steps_file.close()