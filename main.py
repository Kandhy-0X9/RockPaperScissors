# 1. Import the random module.

import random

##welcome the user
print()
print("Welcome User! \nAre you ready for Rock-Paper-Scissors!!")
print()

#initializing scores
computerScore = 0
humanScore = 0

playAgain = True
while playAgain:

    # 2. Generate a random number between 1 and 3 and set it equal to a variable called computer (hint: use the randint() function) 

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

    elif computerChoice == 1 and humanChoice == 3:
        print("Computer wins!")

    elif computerChoice == 2 and humanChoice == 1:
        print("Computer wins!")

    elif computerChoice == 3 and humanChoice == 2:
        print("Computer wins!")

    elif humanChoice > 3 or humanChoice < 0:
        print("That isn't allowed")

    else:
        print("You win!")
        humanScore += 1

    #show scores
    print()
    print("Your score is", humanScore)
        


    ##spacing 
    print()
    print()

    #play again
    #loop

    choice = input("Do you want to play again(yes/no): ").strip().lower()

    if choice == "no":
        playAgain = False
    
print("Thanks for playing")
print()