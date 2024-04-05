
def input_number():
    result = int(input("Enter a Number ")) * 100
    print(result)


num = 100
def input_number2():
    num = 50
    result = int(input("Enter a Number: ")) * num
    print(result)



num = 100

def input_number3():
    global own_num    
    own_num = 50
    result = int(input("Enter a Number: ")) * own_num
    return result

input_number()
input_number2()
input_number3()

print(own_num) # global variable own_num avaliable after the function call. 


