""" Dice value guessing game from Codecademy """

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess



def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is %d!" % max_val

  guess = get_user_guess()

  if max_val < guess:
    print "Invalid Guess!"
  elif guess == 1:
    print "Really?"
  else:
    print "Rolling..."
    sleep(2)
    print "First Roll: %d" % first_roll
    sleep(1)
    print "Second Roll: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result..."
    sleep(0.5)
    
    if guess == total_roll:
      print "Correct!"
    else:
      print "Almost! Try Again."

roll_dice(6)
