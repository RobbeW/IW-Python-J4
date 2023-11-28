# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
    print( " " * i + "*" * (n-i) )
