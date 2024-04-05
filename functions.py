# functions 
# print()
# len()
# input()

# Methods
# list.append()
# list.insert()


# def input_number():
#     return int(input("Enter a number: "))

# input1 = input_number()
# print(input1)
# input2 = input_number()
# print(input2)

# # function arguments 

# def input_number(num):
#     return int(input("Enter a Number: "))*num

# input1 = input_number(10)
# print(input1)


# def input_number2(num1, num2):
#     return int(input("Enter aNumber: ")) * num1 - num2

# input1 = input_number2(10,20) 
# print(input1)

# function return

def print_sum(num1,num2):
    sum = num1 + num2
    print("The Sum is: ", str(sum))

print_sum(10,20)
print_sum(4,2)
print_sum(-1,1)

def is_even(num):
    if(num % 2 == 0):
        return True
   

print(is_even(12))
print(is_even(5))

# function List as Arguments 

def multiply_values(list):
    multiplied_values=[]

    for item in list:
        multiplied_values.append(item * 2)
    return multiplied_values

print(multiply_values([1,2,3]))
print(multiply_values([-4,-8,-10]))