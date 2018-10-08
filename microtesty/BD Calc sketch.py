#program to calculate bend deduction, bend allowance, and possibly some other stuff.
#this is definitely a sketch to start, so we'll see where this goes
#may even turn into something useful  ¯\_(ツ)_/¯

import click
import math
from time import sleep

#shrug = "\ _(ツ)_ /"
#for when we just don't know

k_factor={
   'steel': [ .40, .45, .50],
   'aluminum_soft': [ .33, .40, .50],
   'aluminum_hard': [ .38, .43, .50]
}

def bend_allow():
    material = input("pick a material. either 'steel', 'aluminum_soft', or 'aluminum_hard': ")
    a=float(input("bend angle (how far the material has been bent from it's original flat state): "))
    R=float(input('inside radius: '))
    #K=float(input('k-factor: '))
    T=float(input('material thickness: '))

    if R <=T:
        K=k_factor[material][0]
    elif R>=T and R < 3*T:
        K=k_factor[material][1]
    elif R>3*T:
        K=k_factor[material][2]
    else:
        print("something's wrong")
    #print(K)

    BA=a*(math.pi/180)*(R+(K*T))

    return BA

def bend_deduc():
    #BA=bend_allow()

    material = input("pick a material. either 'steel', 'aluminum_soft', or 'aluminum_hard': ")
    a=float(input("bend angle (how far the material has been bent from it's original flat state): "))
    R=float(input('inside radius: '))
    #K=float(input('k-factor: '))
    T=float(input('material thickness: '))

    if R <=T:
        K=k_factor[material][0]
    elif R>=T and R < 3*T:
        K=k_factor[material][1]
    elif R>3*T:
        K=k_factor[material][2]
    else:
        print("something's wrong")
    #print(K)

    BA=a*(math.pi/180)*(R+(K*T))
    a=math.radians(a)
    BD=2*(R*T)*math.tan(a/2)-BA
    return BD

print("select method: ")
print("1-dend deduction")
print('2-bend allowance')
print('3-EXIT')

selection=int(input('enter method number: '))
while selection <3:
    if selection == 1:
        print( bend_deduc())

    elif selection == 2:
        print( bend_allow())
    elif selection == 3:
        print ('thanks for playing.')
        break
    else:
        print('invalid input. please select a number 1-3')
    selection=int(input('select a calculation or enter 3 to exit.'))
