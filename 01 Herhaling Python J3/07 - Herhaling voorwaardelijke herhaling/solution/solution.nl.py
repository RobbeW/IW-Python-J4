# Initialisatie
aantal = 0
som = 0

# Walrusoperator maakt dit superkort
while (getal := int(input("Geef een getal in: "))) != -1:
    som += getal
    aantal += 1

# Eindweergave
if aantal != 0:
    gem = som / aantal
    print( "Het gemiddelde van de getallen is", round(gem, 2) )
else:
    print("Er werd geen enkel getal ingevoerd.")
