# 1. Import the random module.

import random
import time
from faker import Faker
import os
#import files close

fake = Faker()
print(time.ctime())
##welcome the user
print()
print("Welcome User! \nAre you ready for Rock-Paper-Scissors!!")
print()

##user name for user

#ask the user for his/her name

name_E = input("What is your name? ").lower().replace(" ", "_")
print()

choice = input("Do you want to use your real name? (Yes or No): ").strip().lower()
print()

#create if statement 

if choice == "yes":
    randomNumber = str(random.randint(0, 100))
    fakeName = name_E+randomNumber
    

elif choice == "no":   
    Print = fake.name().lower().replace(" ", "_")
    randomNumber2 = str(random.randint(0, 100))
    fakeName = Print+randomNumber2
    
#end of user name

#initializing scores
computerScore = 0
humanScore = 0
scoreStreak = 0
highestStreak = 0

# Ask user for number of rounds
while True:
    try:
        totalRounds = int(input("How many rounds would you like to play? "))
        if totalRounds > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

currentRound = 0

playAgain = True
while playAgain and currentRound < totalRounds:
    currentRound += 1
    print(f"\n--- Round {currentRound} of {totalRounds} ---")
    
    # load  highest streak from file
    
    streakFile = "streak.txt"
    if os.path.exists(streakFile):
        with open(streakFile, "r") as file:
            try:
                highestStreak = int(file.read().strip())
            except ValueError:
                highestStreak = 0

    # 2. Generate a random number between 1 and 3 and set it equal to a variable called computer (hint: use the randint() function) 
    #welcome user
    print("Welcome", fakeName,"!\n")
    print("The programm is case sensitive, so please use lowercase letters for your answers.")
    print("\nLet's play Rock-Paper-Scissors!\n")

    print()
    computerChoice = random.randint(1 , 3)

    # 3. Using input, get the user's choice where 1 is rock, 2, paper, and 3 is scissors. Store the user's input in a variable called user.

    print("Here is how to play. You pick a number that represents your choice\n 1 for Rock\n 2 for Paper\n 3 for Scissors")
    print()

    humanChoice = int(input("So, what is your choice: "))
    print()
    print("The computer chose", computerChoice)
    print()
    # 4. Use if-statements to determine the winner of the game and print the result.
    
    ### paper (2) beats rock (1)
    ### rock (1) beats scissors (3)
    ### scissors (3) beats paper (2)

    ## If the computer and the user choose the same option, print "It's a tie!". If the computer wins, print "Computer wins!". If the user wins, print "You win!". 
    if computerChoice == humanChoice:
        print("It's a tie!")
        scoreStreak = 0

    elif computerChoice == 1 and humanChoice == 3:
        print("Computer wins!")
        scoreStreak = 0

    elif computerChoice == 2 and humanChoice == 1:
        print("Computer wins!")
        scoreStreak = 0

    elif computerChoice == 3 and humanChoice == 2:
        print("Computer wins!")
        scoreStreak = 0

    elif humanChoice > 3 or humanChoice < 0:
        print("That isn't allowed")
        scoreStreak = 0

    else:
        print("You win!")
        humanScore += 1
        scoreStreak += 1
        if scoreStreak > highestStreak:   # <-- update highest streak
            highestStreak = scoreStreak

    #show scores
    print()
    print("Your score is", humanScore)
        

    ##spacing 
    print()
    print()

    #play again
    #loop

    if currentRound < totalRounds:
        choice = input("Do you want to play again(yes/no): ").strip().lower()
        if choice == "no":
            playAgain = False
    else:
        print("Game over! You've reached the maximum number of rounds.\n")
    

print("Your score is", humanScore)
print("\nYour current win streak is", scoreStreak)
print("Your highest win streak is", highestStreak)

# Save the highest streak to a file
with open(streakFile, "w") as file:
    file.write(str(highestStreak))

print()
print("Thanks for playing", fakeName)
print("Goodbye!")
print(time.ctime())