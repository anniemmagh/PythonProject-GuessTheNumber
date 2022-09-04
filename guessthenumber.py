from random import randrange
import math
lower_bound = int(input("Please enter lower bound: ")) 
upper_bound = int(input("Please enter upper bound: "))

def guess_the_number_user(lower_bound,upper_bound):
    number_to_guess = randrange(lower_bound,upper_bound)
    user_guess = math.inf

    while number_to_guess != user_guess:
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        if user_guess < number_to_guess:
            print("Too small, Try again: ")
        elif user_guess > number_to_guess:
            print("Too big, Try again: ")

guess_the_number_user(lower_bound,upper_bound)