def sum(a, b):
    return a + b

def test():
    if sum(1, 2) != 3:
        print("Error!")
    elif sum(-1, 1) != 0:
        print("Error!")
    elif sum(0, 0) != 0:
        print("Error!")
    else:
        print("All tests passed!")

if __name__ == "__main__":
    test()

def is_two(num):
    return True if num == 2 else False