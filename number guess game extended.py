""" Dice value guessing game written in python.
    Last updated: 19.02.2023 """

from random import randint
import time
import os

#----------------------------------------------------------------------------------
# determmines how often the animation cycle changes values
animate_cycle = 5
# determines the sides of the dice
dice_sides = 6

#----------------------------------------------------------------------------------
# Asks user's guess
def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess

#----------------------------------------------------------------------------------
# Prints the different dice side symbols
def dice_roll_symbol(number):
    match number:
        case 1:
            return "+---------+\n|         |\n|    O    |\n|         |\n+---------+"
        case 2:
            return "+---------+\n|       O |\n|         |\n| O       |\n+---------+"
        case 3:
            return "+---------+\n|       O |\n|    O    |\n| O       |\n+---------+"
        case 4:
            return "+---------+\n| O     O |\n|         |\n| O     O |\n+---------+"
        case 5:
            return "+---------+\n| O     O |\n|    O    |\n| O     O |\n+---------+"
        case 6:
            return "+---------+\n| O     O |\n| O     O |\n| O     O |\n+---------+"

#----------------------------------------------------------------------------------
# Clears the last 5 lines to remove the previously printed cube
def clear_cube(wait_time):
    time.sleep(wait_time)
    for i in range(5):
        print ("\033[A                             \033[A") #clears last line

#----------------------------------------------------------------------------------
# Animates rolling the dice
def animate(n):
    for i in range(n):
        value = randint(1, 6)
        print(dice_roll_symbol(value))
        clear_cube(0.5)

#----------------------------------------------------------------------------------
# Main function
def roll_dice(number_of_sides):
    os.system("cls")
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print ("The maximum possible value is %i!" % max_val)

    guess = get_user_guess()

    if max_val < guess:
        print ("Invalid Guess!")
    elif guess == 1:
        print ("Really?")
    else:
        print ("Rolling...")
        time.sleep(1.5)
        print ("First Roll:")
        animate(animate_cycle)
        print(dice_roll_symbol(first_roll))
        print("Second Roll:")
        animate(animate_cycle)
        print(dice_roll_symbol(second_roll))
        total_roll = first_roll + second_roll
        print ("Result...")
        time.sleep(1)
    
        if guess == total_roll:
            print ("Correct!")
        else:
            print ("Almost! Try Again.")

#----------------------------------------------------------------------------------
roll_dice(dice_sides)
