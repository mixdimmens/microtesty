"""
this program will compair user input to random numbers, 
bro.
builtfor codeacademy project thingy
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("gimme a number (btwn 1-12)"))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print ('the maximum possible value is %d') % (max_val)
  guess = get_user_guess()
  if guess >12:
    print ('guess exceeds maximum possible value. max possible value is %d.') % (max_val)
  else:
    print ('rolling'),
    sleep(1)
    print ('.'),
    #sleep(1)
    print ('.'),
    #sleep(1)
    print ('.')
    sleep(1)
    print ('first roll value: %d') % (first_roll)
    sleep(1)
    print ('second roll value: %d') % (second_roll)
    sleep(1)
    total_roll= first_roll+second_roll
    print ('total is: %d') % (total_roll)
    sleep(1)
    if guess == total_roll:
      print ('you got it, boss!'),
      sleep(.5)
      print ('good job!')
    else:
      print ('better luck next time, loser')
      
      
    
    
    
    
roll_dice(6)