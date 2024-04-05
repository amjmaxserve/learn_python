try:
    name = 'Arjun'
    print('my name is: ' + nmae)
except:
    print('Something went wrong')

print('All done!')

# Errors in python

# ZeroDivisionError AssertionError IndentationError ValueError AttributeError StopIteration
# TypeError IndexError RuntimeError SystemError KeyError OverflowError TabError ReferenceError UnicodeError

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by Zero")
except ValueError:
    print("please Enter an Intiger")
except:
    print("Something Went Wrong!..")
    
print("All Done!")


def calculate_user_input():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except ZeroDivisionError:
        print("Cannot divided by Zero.")
    except:
        print("Something went Wrong")
    return None

calculate_user_input()

# raise error automatically

def calculate_user_input2():
    try:
        x = int(input("Enter a number: "))
        y = 1 / x
        print(y)
    except:
        print("Something went Wrong")
        raise
    return None

calculate_user_input2()

# assert
# raises an AssertionError in the expression evaluates to a falsy value

import math
x = int(input("Enter a number "))
assert x>= 0
x = math.sqrt(x)
print("Result: ", x)
