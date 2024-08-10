# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( 2 * n - 1 ):
    if i == 0 or i == 2*n-2:
        print(" " * (n - 1) +"x")
    else:
        a = max( n - i - 1, i - n + 1 )
        b = min( 2 * i + 1, 4 * n - 3 - 2* i )

        print( " " * a + "x" + " " * (b-2) + "x" )
