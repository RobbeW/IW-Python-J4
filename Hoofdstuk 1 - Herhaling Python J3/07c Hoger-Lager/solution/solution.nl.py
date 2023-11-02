import random
random.seed(123)

# Initialisatie
getal = random.randint( 1, 1000 )
print(getal)
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
        if aantal == 1:
            print("Je hebt het meteen geraden!")
        else:
            print("Je hebt het geraden in", aantal, "pogingen!")
