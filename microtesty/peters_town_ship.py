#circular string test

print('START')

peters = 'people are perfect nouns. but sometimes they get named afer towns. '
town = 'towns are places. they are not things. towns can be named after things, though. '
ship = 'things are objects. they are inatimate. but objects can be like people. '

print(town)

town_ship = town+ship
peters_town = peters+town
peters_town_ship = ship+peters_town+town_ship

print(peters_town_ship)

town_ship_peters = town+ship+peters

print(town_ship_peters)

print(' ')
peterstownship = peters+town_ship
print(peterstownship)
print(' ')

print('END')