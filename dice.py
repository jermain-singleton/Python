import random

def play_dice():
    
    def play_again():
        i = input('Enter 1 to play. Enter 2 to quit: ')
        if i == '1':
            play_dice()
        if i == '2':
            print("Goodbye"  )

    secret = random.randint(1,6)
    guesses = []
    
    while len(guesses) < 3:
        guess = int(input("Guess 1 thru 6: "))
        if guess == secret:
            print("Correct")
            break
        elif guess > secret:
            print("Too high, guess lower")
        elif guess < secret:
            print("Too low, guess higher")
            guesses.append(guess)
    play_again()
play_dice()

