# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
som = 0
i = 0
while i < n:
    som += 1 / 2**(i + 1)
    i += 1

# Uitvoer
print("De som van de eerste", n, "termen is", round(som, 6 ) )
