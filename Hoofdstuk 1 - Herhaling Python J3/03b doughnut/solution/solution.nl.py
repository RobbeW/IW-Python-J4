PI = 3.141592

# Invoer van de variabelen
r = float( input( 'Geef de kleine straal in:' ) )
R = float( input( 'Geef de grote straal in:' ) )

# Berekeningen
A = round( 4 * PI**2 * r * R, 3)
V = round( 2 * PI** 2 * r ** 2 * R, 3)

# Uitvoer
print( 'Oppervlakte:', A, 'cm²' )
print( 'Volume:', V, 'cm³' )
