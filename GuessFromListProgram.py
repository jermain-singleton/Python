# imports the random module
import random, os
# main function
def play_again():  
    # list the guess are chosen from
    Guess = ['Lucky', 'Looking Good', 'All of board', 'No so Lucky', 'Today will be Ominus', 'The end is not near']
    # clears the screen
    os.system('cls')
    print("Here is your Guess for the day")
    print(random.choice(Guess))  # random list option chosen and printed
    
    # below ask to play again and a way to exit the program
    print("\nWould you like another guess?")
    answer = input("PRESS enter or no to quit: ")
    if answer == 'no':
        run = False
    else:
        play_again()

play_again()
