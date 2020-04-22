import random

print("I will ask for two numbers, you will guess what the number is because it will be in between of the two numbers you pick.")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

systemPicked = random.randint(num1, num2)
userGuess = systemPicked - 1

if systemPicked != userGuess:
    while systemPicked != userGuess:
        userGuess = int(input("Enter your guess: "))
    
        if userGuess < systemPicked:
            print("---You guessed too low stuuuuuuuuuuuupid /\/\/\/\/\/\/\/\/\/")
        elif userGuess > systemPicked:
            print("---YA GUESSED TOO HIGH DUMMY")
        else:
            print("---Wow ur a big dummy it took you more than one try. U finally got it right.")
     
else:
#if(count == 1)
    print("---WOW you got it first try")
#else:
 #   print("")