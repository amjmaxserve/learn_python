name = "Lydia"
ages = [56,72,24,46]
ages2 = ages
ages[0]=92
print(ages2[0])

age=22

def multiply(num):
    num *= 2
    print("In multiply * 2: ", str(num))

print("Age: ", age)
multiply(age)

nums = [1,2,3]
print("current List: ", nums)

def change_first_item(list):
    list[0]= 9

change_first_item(nums)
print("list after change: ",nums)