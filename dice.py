# import non builtin module
import random


#calls the main dice game
def play_dice():
    
    
    # function to ask the user to play again
    def play_again():
        i = input('Enter 1 to play. Enter 2 to quit: ')
        if i == '1':
            play_dice()
        if i == '2':
            print("Goodbye"  )

    # variable for random number generator  
    secret = random.randint(1,6)
    guesses = []  # list var
    
    # where the loop begins and program
    while len(guesses) < 3:  # max of three chances to win
        guess = int(input("Guess 1 thru 6: "))  #guess a number btw one and six
        if guess == secret:
            print("Correct")
            break
        elif guess > secret:
            print("Too high, guess lower")
        elif guess < secret:
            print("Too low, guess higher")
            guesses.append(guess)  # adds number of guesses to the list
    play_again()  # if user selects the option play again or exit the loop
play_dice()

