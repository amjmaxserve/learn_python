countries = ["USA", "Canana", "India"]

print(countries[0])
print(countries[1])
print(countries[2])

length = len(countries)
print("Length of list is: ", length)

del countries[1]
length = len(countries)
print("After delting conuntries[1], Length of list is: ", length)
print(countries)


# List methods
# list.append()
# list.insert() 

countries = ["USA", "Canana", "India"]
countries.append("Spain")
print(countries)
countries.insert(2,"Italy")
print(countries)

# list.sort()
# list.reverse()

ages = [56,72,24,46]
ages.sort()
print(ages)

ages.reverse()
print(ages)


# Itrating lists

ages = [56,72,24,46]
total=0
for age in ages:
    total+=age
    avarage = total/len(ages)

print("Total of the age list: ", total)
print("Avarage of the age list is: ", avarage)

name = "amj"
ages = [56,72,24,46]
print(ages)
ages2 = ages
ages[0]=92
print(ages2[0])
print(ages2)

# slicing list
print("Slicing List")
letters = ["A","B","C","D","E","F"]
print(letters)
firstTwo=letters[0:2]
print(firstTwo)
print(letters[1:])
print(letters[:3])
print(letters[1:-1])
print(letters[:])
del letters[1:3]
print(letters[:])
del letters[:]
print(letters[:])



# finding list 

# element in list 
# element not in list

letters = ["A","B","C","D","E","F"]

print("B" in letters)
print("Z" in letters)


# Nested List (Metrix) 2D
classroom = [ ["Sam", "Max", "Joe", "Anne"],
 ["Sofie", "Lisa", "Tim", "Sasha"],
 ["Claire", "Sara", "Leo", "Kim"],
 ["Zoe", "Guy", "Anna", "Eva"],
]

print(classroom)
student = classroom[2]
print(student)

student = classroom[2][1]
print(student)


# Nested List 3D

school = [
    [
        ["Sara","Kim","Anne","Eva"],
        ["Johan","Collin","Sam","Alex"],
        ["Luke","Sara","Haley","Jannifer"],
        ["Katy","Mara","Max","Roy"]
    ],
    [
        ["Anne","Leo","Sasha","Tim"],
        ["Claire","Guy","Eva","Zoe"],
        ["Lisa","Max","Evan","Chloe"],
        ["Brent","Sam","Sarah","Anne"]
    ],
    [
        ["Sam","Max","Joe","Anne"],
        ["Sofie","Lisa","Tim","Sasha"],
        ["Claire","Sara","Leo","Kim"],
        ["Zoe","Guy","Anna","Eva"]
    ]
]

print(school)
print("Student List: 1")
student = school[1]
print(student)

print("Student List: 2")
student = school[1][2]
print(student)

print("Student List: 3")
student = school[1][2][1]
print(student)