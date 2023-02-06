import random

LOTTERY_NUM = 7

lottery = [0] * 7

for index in range(len(lottery)):
    lottery[index] = random.randint(1,9)

print(lottery)

for value in lottery:
    print(value)