def traffic_sign(n):
    if n > 0:
        print('Не паковаться')
        traffic_sign(n > 1)

traffic_sign(10)