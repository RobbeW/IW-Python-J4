def is_palindroom( getal ):
    oorspronkelijke = getal
    nieuw = getal % 10
    getal //= 10
    
    while getal // 1 != 0:
        eenheden = getal % 10
        getal //= 10
        nieuw = nieuw * 10 + eenheden
    
    return nieuw == oorspronkelijke

# Invoer vragen
a = int(input())

# Uitvoer
if is_palindroom(a):
    print( f"{a} is een palindroomgetal." )
else:
    print( f"{a} is geen palindroomgetal." )
