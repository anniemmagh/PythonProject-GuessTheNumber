from random import randrange

lower_bound = int(input("Please enter lower bound: ")) 
higher_bound = int(input("Please enter higher bound: "))

def guess_the_number_user(lower,higher):
    number_to_guess = randrange(lower,higher)