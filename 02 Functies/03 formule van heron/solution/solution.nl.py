import math

def oppervlakte( a, b, c ):
    s = 1 / 2 * ( a + b + c )
    A = math.sqrt( s * (s - a) * ( s - b ) * ( s - c ) )
    return round( A, 2 )

# invoer
a = int(input("Geef de eerste zijde in: "))
b = int(input("Geef de tweede zijde in: "))
c = int(input("Geef de derde zijde in: "))

# verwerking
A = oppervlakte(a, b, c)

# uitvoer
print(f"De oppervlakte bedraagt {A} cm².")
