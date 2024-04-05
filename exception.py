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