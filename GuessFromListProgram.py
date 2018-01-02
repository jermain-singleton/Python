import random, os
def play_again():    
    Guess = ['Lucky', 'Looking Good', 'All of board', 'No so Lucky', 'Today will be Ominus', 'The end is not near']
    os.system('cls')
    print("Here is your Guess for the day")
    print(random.choice(Guess))
    
    
    print("\nWould you like another guess?")
    answer = input("PRESS enter or no to quit: ")
    if answer == 'no':
        run = False
    else:
        play_again()

play_again()