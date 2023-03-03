numbers = [1,2,3,4,5,10,34,8]

def find_more_n(list_numbers, num_n):
    for num in list_numbers:
        if num_n < num:
            print(num)
        
find_more_n(numbers, 5)
        

