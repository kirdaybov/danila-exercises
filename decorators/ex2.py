def check(input_func):
    def output_func(*args):
        input_func(*args)
    return output_func

@check
def print_person(name, age):
    print(f'Name: {name}  Age: {age}')

print_person('Danila', 24)

def minus_one(input_func):
    def output_func(*args):
        num1 = int(args[0])
        num2 = int(args[1])
        num1 -= 1
        num2 -= 1
        input_func(num1, num2)
    return output_func
        
@minus_one
def foo(number1,number2):
    print(f' First number minus one = {number1}, second number minus one = {number2} ')

foo(2,3)