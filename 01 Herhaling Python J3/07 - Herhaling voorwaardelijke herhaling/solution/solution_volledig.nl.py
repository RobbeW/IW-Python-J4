# Initialisatie
aantal = 0
som = 0

# Klassieke while lus
getal = int(input("Geef een getal in: "))
while getal != -1:
    som += getal
    aantal += 1
    getal = int(input("Geef een getal in: "))

# Eindweergave
if aantal != 0:
    gem = som / aantal
    print( "Het gemiddelde van de getallen is", round(gem, 2) )
else:
    print("Er werd geen enkel getal ingevoerd.")
