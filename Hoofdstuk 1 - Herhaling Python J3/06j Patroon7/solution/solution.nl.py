# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
    a = n - i - 1
    b =  i + 1
    print( " " * a + "*" * b)

for i in range( n - 1):
    a = i + 1
    b = n - i - 1
    print( " " * a + "*" * b )