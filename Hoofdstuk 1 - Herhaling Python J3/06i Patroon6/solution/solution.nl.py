# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
print()
for i in range( n ):
    print( " " * (n-i-1) + (2*i +1 ) * "*" )
