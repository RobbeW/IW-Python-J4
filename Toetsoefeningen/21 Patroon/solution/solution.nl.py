# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n):
    print(" "*i + "*" + " "*(2*n - 2 - 2*i)+ "*")
