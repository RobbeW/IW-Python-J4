import math

def oppervlakte( a, b, c, d ):
    s = 1 / 2 * ( a + b + c + d)
    A = math.sqrt( (s - d) * (s - a) * ( s - b ) * ( s - c ) )
    return round( A, 2 )

# invoer
a = int(input("Geef de lengte van zijde a in: "))
b = int(input("Geef de lengte van zijde b in: "))
c = int(input("Geef de lengte van zijde c in: "))
d = int(input("Geef de lengte van zijde d in: "))

# verwerking
A = oppervlakte(a, b, c, d)

# uitvoer
print(f"De oppervlakte bedraagt {A} cm².")
