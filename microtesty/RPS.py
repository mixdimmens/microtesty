"""
rocks, paper, scissors, bro.
you vs. acomputer. who will win?
probably not you. 

"""

#from random import randint
import random
from time import sleep

options = ['rook', 'papel', 'scabies']

message = {
  'tie' : 'what a snoozer',
  'won' : 'ya did it, dingus!',
  'lost' : 'ya lost it, bonehead!'
}

def decide_win(user_in, comp_in):
    print ('you selceted: ' + user_in)
    print ('the computer went with: ' + comp_in)
    if user_in == comp_in:
        print(message['tie'])
    elif user_in == options[0] and comp_in == options[2]:
        print (message['won'])
    elif user_in == options[1] and comp_in == options[0]:
        print (message['won'])
    elif user_in == options[2] and comp_in == options[1]:
        print (message['won'])
    else:
        print (message['lost'])

def play_bro():
    count = 0
    while count<3:
        print('rook, papel, scabies. ')
        user_in = input('pick one, bro: ')
        user_in = user_in.lower()
        #comp_in = options[randint(0.2)]
        comp_in = options[random.randint(0,2)]
        decide_win(user_in,comp_in)
        sleep(2)
        count+=1


play_bro()



    