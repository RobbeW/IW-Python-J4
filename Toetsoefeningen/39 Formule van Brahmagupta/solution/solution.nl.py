import math

def oppervlakte( a, b, c, d ):
    s = 1 / 2 * ( a + b + c + d)
    A = math.sqrt( (s - d) * (s - a) * ( s - b ) * ( s - c ) )
    return round( A, 2 )

# invoer
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# verwerking
A = oppervlakte(a, b, c, d)

# uitvoer
print(f"De oppervlakte bedraagt {A} cm².")
