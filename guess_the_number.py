#Program Name: Guess The Number
#Programmer: Reyansh Patil (reyanshpatil1010)
#Date: 25/12/2024 (Christmas 2024)

import random

print("Welcome to Guess The Number game (between 1-100)")


r = random.randint(1, 100)

def guess_number():

    a = int(input("Whats your guess number?:"))
    if a == r:
        print("Spot on, you guessed it correctly!!..")
        return True

    elif a > r:
        print("Ah, good luck next time. Hint: Try a lower number")

    elif a < r:
        print("Ah, good luck next time. Hint: Try a higher number")

    return False

while True:
    guessed = guess_number()

    if guessed == True:
       restart = input ("Do you want to start new Guess The Number game? (y/n)")
       if restart == "y" or restart == "Y":
          r = random.randint(1, 100)
       else:
          print("Thank you for playing.")
          break
        
