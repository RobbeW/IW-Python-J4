import math

# Invoer vragen
tweea = float( input( 'Geef de lengte van de lange as in: ') )
tweeb = float( input( 'Geef de lengte van de korte as in: ') )

# Berekeningen
a = tweea / 2
b = tweeb / 2
h = ( a - b )**2 / ( a + b )**2
P = math.pi * ( a + b ) * ( 1 + 3 * h / ( 10 + math.sqrt(4 - 3 * h ) ) )

# Uitvoer
print()
print( "De omtrek van de ellips meet bij benadering:", round( P, 2 ), "cm." )

