# Invoer
snelheid = float( input( 'Geef de snelheid in km/u in: ' ) )
a = float( input( 'Geef de remvertraging in m/s² in: ' ) )

# Verwerking
v = snelheid / 3.6

remweg = v**2 / ( 2 * a )

# Uitvoer
print( 'Remweg:', round( remweg, 3 ), 'm.' )
