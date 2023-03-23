def check(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result.isdigit():
            print('Это число')
            result = int(result)
            if result > 0: print('Положительное')
            return result
        else:
            print('Это не число')
    return output_func

@check
def sum(a,b):
    return str(a + b)

result1 = sum('а','20')
print(result1)