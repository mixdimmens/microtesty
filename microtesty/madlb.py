"""
This program generates passages that are generated in mad-lib format
users input the shit (words) and the program prints the
story
Author: Katherin 
program: mostly katherin
"""

# The template for the story

import time

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."


print('madlibs initiating...')

name = input('enter a name: ')

adj_1 = input('enter an adjective: ')
adj_2 = input('enter another: ')
adj_3 = input('and another, bro: ')

verb = input('gimme a verb: ')

noun_1 = input('noun, please: ')
noun_2 = input('one more, cheif: ')

animal = input('an animal: ')
food = input('a food: ')
froot = input('a fruit, actually: ')
print("not that you'd know what that is. ")
time.sleep(.2)
supper = input('someone predictable: ')
state = input('enter a state or nation-state: ')
desert = input('baked alaska type item: ')
year = input('anno: ')
noun_3 = input('nounyza?: ')

print (STORY) % (name, adj_1, adj_2, animal, food, verb, noun_1, froot, adj_3, name, supper, name, desert, adj_2, name, year, noun_2, noun_3)



















