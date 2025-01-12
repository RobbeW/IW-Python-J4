import random

def hogerLager(getal):
    aantal = 0
    geraden = False
    while not geraden:
        gok = int( input( "Gok een getal: " ) )
        aantal += 1
        if gok > getal:
            print( "Het getal is lager dan", gok )
        elif gok < getal:
            print( "Het getal is hoger dan", gok )
        else:
            geraden = True
    return aantal


# Initialisatie
getal = random.randint( 1, 1000 )
aantal = hogerLager(getal)

if aantal == 1:
    print("Je hebt", getal, "meteen geraden!")
else:
    print("Je hebt", getal, "geraden in", aantal, "pogingen!")
