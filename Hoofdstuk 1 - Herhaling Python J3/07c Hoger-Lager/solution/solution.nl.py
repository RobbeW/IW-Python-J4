import random

# Initialisatie
getal = random.randint( 1, 1000 )

# Herhaling
aantal = 0
geraden = False
while not geraden:
    gok = int( input( "Gok een getal: " ) )
    aantal += 1
    if gok > getal:
        print( "Lager" )
    elif gok < getal:
        print( "Hoger" )
    else:
        geraden = True
        print("Je hebt het geraden in", aantal, "pogingen!")
