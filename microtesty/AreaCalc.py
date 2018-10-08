#area and volume calculator for rectangels, trianges, circles, rectangular prisims, cylnders, and spheres
#users select shape and input requiered dimensional values, program outputs area or volume

print("hey hey, it's an area and volume calculator!")
print('pick the shape you wish to calculate, then input the requiered dimensions. ')
print('shape options: ')
print(' 1-rectangle')
print(' 2-triange')
print(' 3-circle')
print(' 4-rectangular prisim')
print(' 5-cylnder')
print(' 6-sphere')
print(' 7-EXIT PROGRAM')
shape_selection = int(input('input option (by number): '))

#while shape_selection<7:
if shape_selection == 1:
    width = float(input('input rectangle width: '))
    height = float(input('input rectangle height: '))
    area = width*height
    print(area)

elif shape_selection == 2:
    base = float(input('input base length: '))
    height = float(input('input triangle height: '))
    area = base*height
    print(area)

elif shape_selection == 3:
    option = input('diameter or radius?: ')
    option = option.lower()
    option = option[0]
    if option == 'r':
        rad = float(input('input radius: '))
        area = rad*2*3.14159
        print(area)
    elif option == 'd':
        dia = float(input('input diameter: '))
        area = dia*3.14159
        print(area)
    else:
        print('invalid input. sorry, bro. ')

elif shape_selection == 4:
    length = float(input('input length: '))
    width = float(input('input width: '))
    height = float(input('input height: '))
    vol = length*width*height
    print(vol)

elif shape_selection == 5:
    option = input('diameter or radius?: ')
    option = option.lower()
    option = option[0]
    if option == 'r':
        rad = float(input('input radius: '))
        height = float(input('input height: '))
        vol = rad*2*3.14159*height
        print(vol)
    elif option == 'd':
        dia = float(input('input diameter: '))
        height = float(input('input height: '))
        vol = dia*3.14159*height
        print(vol)
    else:
        print('invalid input. sorry, bro. ')
elif shape_selection == 6:
    option = input('diameter or radius?: ')
    option = option.lower()
    option = option[0]
    if option == 'r':
        rad = float(input('input radius: '))
        vol = rad**3*3.14159*(4/3)
        print(vol)
    elif option == 'd':
        dia = float(input('input diameter: '))
        vol = (dia/2)**3*3.14159*(4/3)
        print(vol)
    else:
        print('invalid input. sorry, bro. ')
    
   # shape_selection = 0d

print('exiting program. danke!')
