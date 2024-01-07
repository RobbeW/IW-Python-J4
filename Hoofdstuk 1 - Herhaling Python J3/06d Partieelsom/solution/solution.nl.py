# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
som = 0
for i in range(n):
    som += 1 / 2**(i + 1)

print("De som van de eerste", n, "termen is", round(som, 6 ) )