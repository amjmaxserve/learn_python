secret_number = 2
guess = int(input("Guess a Number: "))
while guess != secret_number:
    guess=int(input("Guess a Number: "))
else:
    print("Congratulations, You got it!") 
