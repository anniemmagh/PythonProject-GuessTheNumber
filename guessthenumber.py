from random import randrange
import math
lower_bound = int(input("Please enter lower bound: ")) 
higher_bound = int(input("Please enter higher bound: "))

def guess_the_number_user(lower,higher):
    number_to_guess = randrange(lower,higher)
    user_guess = math.inf

    while number_to_guess != user_guess:
        user_guess = int(input("Guess the number between"))