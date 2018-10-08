#attempt at an intelligent workflow for a bend calculator. will have several different workflows:
#  1- calculating for one design. i.e select one material type, thickness, and calculation type to repeatedly 
# calculate with those parameters for multipule bends. 
# 2- raw input. i.e. enter all parameters for every calculation. 
# 3- maybe something else

import math
import argparse




k_factor={
   'steel': [ .40, .45, .50],
   'aluminum_soft': [ .33, .40, .50],
   'aluminum_hard': [ .38, .43, .50]
}
def bend_allow(a, R, K, T):
    BA=a*(math.pi/180)*(R+(K*T))
    return BA

def bend_deduct(a, R, K, T, BA):
    #BA=a*(math.pi/180)*(R+(K*T))
    a=math.radians(a)
    BD=2*(R*T)*math.tan(a/2)-BA
    return BD

# method for selecting workflow:
#  
print('workflow options: ')

menu_selection = input('select an option: ')


while menu_selection != 'EXIT':
#need a way to exit this loop!
    if menu_selection == 'designwise':
        a=float(input("bend angle (how far the material has been bent from it's original flat state): "))
        R=float(input('inside radius: '))
        T=float(input('material thickness: '))

        material = input("pick a material. either 'steel', 'aluminum_soft', or 'aluminum_hard': ")

        if R <=T:
            K=k_factor[material][0]
        elif R>=T and R < 3*T:
            K=k_factor[material][1]
        elif R>3*T:
            K=k_factor[material][2]
        else:
            print("something's wrong")


        calc_type = input('select calculation (ba or bd): ')

        if calc_type == 'ba':
            print(bend_allow(a,R,K,T))
        elif calc_type == "bd":
            print(bend_deduct(a, R, K, T, bend_allow(a, R, K, T)))

        #need to figure out how to let the user input to end the loop, too!