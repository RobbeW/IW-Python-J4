# Initialisatie
aantal = 0
som = 0

# Lus
flag = True
while flag:
    getal = int( input( "Geef een getal in: " ) )
    if getal != -1:
        som += getal
        aantal += 1
    else:
        flag = False

# Eindweergave
if aantal != 0:
    gem = som / aantal
    print( "Het gemiddelde van de getallen is", round(gem, 2) )
else:
    print("Er werd geen enkel getal ingevoerd.")
