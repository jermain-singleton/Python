"""Game to guess stuff of 8 options"""
import random
import os
#create function with a parameter that has guess number conditions
def guess(guess):
    r = guess
    if guess == 1:
        print("The skies are ominus")
    elif guess == 2:
        print('Pick a path')
    elif guess == 3:
        print("Delays in the future")
    elif guess == 4:
        print('No luck')
    elif guess == 5:
        print("Days ahead are looking good")
#parameter to get a random guess option
r = random.randint(1, 5)
guess(r)
