def select(input_func1):    
    def output_func():      
        print("****stars****")  
        input_func1()                
        print("*****************")

    return output_func     
 

@select         
def kirill():
    print("Hello Kirill!")
 
kirill()

