def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

print(multiply(7,4))