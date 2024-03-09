# Invoer van een getal
getal = int( input( 'Geef een getal van 2 cijfers in: ' ) )

# Bepalen van de eenheden en tientallen
e = getal % 10
t = int( ( getal - e ) / 10 )

# Bepalen van het spiegelbeeld
spiegelbeeld = e * 10 + t

# Uitvoer
print('Het spiegelbeeld van', getal, 'is', spiegelbeeld )