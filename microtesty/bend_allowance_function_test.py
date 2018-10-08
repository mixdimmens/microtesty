import math


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

    

print(bend_allow())
