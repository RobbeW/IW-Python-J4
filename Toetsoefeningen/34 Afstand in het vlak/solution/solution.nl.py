import math

# Programmeer hier je functie
def afstand( x1, y1, x2, y2 ):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return round(d, 2)

# Alle coördinaten vragen
xA = float( input( "Geef de x-coördinaat van punt A in: " ) )
yA = float( input( "Geef de y-coördinaat van punt A in: " ) )
xB = float( input( "Geef de x-coördinaat van punt B in: " ) )
yB = float( input( "Geef de y-coördinaat van punt B in: " ) )
xC = float( input( "Geef de x-coördinaat van punt C in: " ) )
yC = float( input( "Geef de y-coördinaat van punt C in: " ) )

# Bepaal nu welke soort driehoek het is
AB = afstand(xA, yA, xB, yB)
AC = afstand(xA, yA, xC, yC)
BC = afstand(xB, yB, xC, yC)

if AB == AC and AB == BC:
    print("Driehoek ABC is gelijkzijdig.")
elif AB == AC or AB == BC or AC == BC:
    print("Driehoek ABC is gelijkbenig.")
else:
    print("Driehoek ABC is ongelijkbenig.")