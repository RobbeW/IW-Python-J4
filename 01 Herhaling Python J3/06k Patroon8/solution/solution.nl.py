# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( 2 * n - 1 ):
    a = max( n - i - 1, i - n + 1 )
    b = min( 2 * i + 1, 4 * n - 3 - 2* i )

    print( " " * a + "*" * b)
