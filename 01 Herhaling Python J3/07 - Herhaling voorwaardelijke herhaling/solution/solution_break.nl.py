# Initialisatie
aantal = 0
som = 0

# While True statement met een break
while True:
    getal = int(input("Geef een getal in: "))
    if getal == -1:
        break
    som += getal
    aantal += 1

# Eindweergave
if aantal != 0:
    gem = som / aantal
    print( "Het gemiddelde van de getallen is", round(gem, 2) )
else:
    print("Er werd geen enkel getal ingevoerd.")
