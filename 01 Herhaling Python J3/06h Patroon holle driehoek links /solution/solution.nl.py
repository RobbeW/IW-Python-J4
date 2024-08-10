# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
    if i == 0 or i >= n-2:
        print( "X" * (n-i) )
    else:
        print( "X" + " " * (n-i-2) + "X")
