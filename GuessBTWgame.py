import random
import os
import time


def play_game():
    def play_again():
        os.system('cls')
        again = str(input("""
Would you like to play again:
Enter 1 for Yes Enter 2 for No  
"""))
        if again == '1':
            play_game()
        else:
            print("Goodbye")
            pass

    attempts = 5
    sec_num = random.randint(1,10)
    print("""
   *******Guessing Game*********
5 guess for a number 1 through 10
""")
    for guess in range(attempts):
        guess = int(input("> "))
        if guess > sec_num:
            print("Guess lower")
        elif guess < sec_num:
            print("Guess Higher")
        if guess == sec_num:
                print("You Win")
                time.sleep(2) 
                play_again()
    play_again()            
   
play_game()

        
            