import math

# Invoer van variabelen
a = float(input("Geef de eerste afstand in: "))
c = float(input("Geef de tweede afstand in: "))

# Berekening
b = round( math.sqrt( c**2 - a**2 ), 3)

# Uitvoer
print("Dit belfort is", b, "m hoog.")
