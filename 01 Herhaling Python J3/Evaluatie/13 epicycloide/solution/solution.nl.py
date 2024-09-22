import math

# Invoer vragen
r_large = float( input( 'Geef de lengte van de grote straal in: ' ) )
r_small = float( input( 'Geef de lengte van de kleine straal in: ' ) )

# Berekeningen
k = r_large / r_small
A = ( k + 1 ) * ( k + 2 ) * math.pi * r_small**2
A = round( A, 3 )

# Uitvoer
print( "De oppervlakte van de epicycloïde is:", A, "cm²." )
