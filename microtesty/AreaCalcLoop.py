"""
area and volume calculator for rectangels, trianges, circles, rectangular prisims, cylnders, and spheres
users select shape and input requiered dimensional values, program outputs area or volume.
started in codeacademy and expanded
"""

print("hey, hey! it's an area and volume calculator!")
print('pick the shape you wish to calculate, then input the requiered dimensions. ')
print('shape options: ')
print(' 1-rectangle')
print(' 2-triange')
print(' 3-circle')
print(' 4-rectangular prisim')
print(' 5-cylnder')
print(' 6-sphere')
print(' 7-REPRINT LIST')
print(' 8-EXIT PROGRAM')
shape_selection = int(input('input option (by number): '))

while shape_selection<8:
    if shape_selection == 1:
        print('rectangle area selected.')
        width = float(input('input rectangle width: '))
        height = float(input('input rectangle height: '))
        area = width*height
        print('rectangle area: '),
        print(area)

    elif shape_selection == 2:
        print('triangle area selected. ')
        base = float(input('input base length: '))
        height = float(input('input triangle height: '))
        area = base*height
        print('triangle area: '),
        print(area)

    elif shape_selection == 3:
        print('circle area selected. ')
        option = input('diameter or radius?: ')
        option = option.lower()
        option = option[0]
        if option == 'r':
            rad = float(input('input radius: '))
            area = rad**2*3.14159
            print('circle area: '),
            print(area)
        elif option == 'd':
            dia = float(input('input diameter: '))
            area = (dia/2)**2*3.14159
            print('circle area: '),
            print(area)
        else:
            print('invalid input. sorry, bro. ')
            shape_selection = 3
        #print('circle area: '),
        #print(area)
        

    elif shape_selection == 4:
        print('rectangular prisim volume selected. ')
        length = float(input('input length: '))
        width = float(input('input width: '))
        height = float(input('input height: '))
        vol = length*width*height
        print('rectangular prism volume: '),
        print(vol)

    elif shape_selection == 5:
        print('cylnder volume selected. ')
        option = input('diameter or radius?: ')
        option = option.lower()
        option = option[0]
        if option == 'r':
            rad = float(input('input radius: '))
            height = float(input('input height: '))
            vol = rad**2*3.14159*height
            print('cylnder volume: '),
            print(vol)
        elif option == 'd':
            dia = float(input('input diameter: '))
            height = float(input('input height: '))
            vol = (dia/2)**2**3.14159*height
            print('cylnder volume: '),
            print(vol)
        else:
            print('invalid input. sorry, bro. ')
        #print('cylnder volume: '),
        #print(vol)
        
    elif shape_selection == 6:
        print('sphere volume selected. ')
        option = input('diameter or radius?: ')
        option = option.lower()
        option = option[0]
        if option == 'r':
            rad = float(input('input radius: '))
            vol = rad**3*3.14159*(4/3)
            print('sphere volume: '),
            print(vol)
        elif option == 'd':
            dia = float(input('input diameter: '))
            vol = (dia/2)**3*3.14159*(4/3)
            print('sphere volume: '),
            print(vol)
        else:
            print('invalid input. sorry, bro. ')
        #print('sphere volume: '),
        #print(vol)
    
    elif shape_selection == 7:
        print('shape options: ')
        print(' 1-rectangle')
        print(' 2-triange')
        print(' 3-circle')
        print(' 4-rectangular prisim')
        print(' 5-cylnder')
        print(' 6-sphere')
        print(' 7-REPRINT LIST')
        print(' 8-EXIT PROGRAM')
    
    else:
        print('invalid selection, sorry bro. ')
    shape_selection = int(input('input calculation option by number (to see list enter 7): '))
    #shape_selection = int(shape_selection)

print('exiting program. danke!')
