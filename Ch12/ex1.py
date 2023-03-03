def recursive_printing(n):
    if n > 0:
        print(n)
        recursive_printing(n - 1)

recursive_printing(10)