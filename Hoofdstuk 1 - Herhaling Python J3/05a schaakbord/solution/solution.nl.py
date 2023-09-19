# Invoer
k = int( input( "Geef het kolomnummer:" ) )
r = int( input( "Geef het rijnummer:" ) )

# Verwerking en uitvoer
if ( k + r ) % 2 == 0:
    print( 'Een donker gekleurd veld' )
else:
    print( 'Een licht gekleurd veld' )
