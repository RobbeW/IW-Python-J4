# Gegevens vragen
getal = int( input( 'Geef het getal in: ' ) )
kleinste = getal
grootste = getal
som = getal

# Berekening
for _ in range(9):
    getal = int( input( 'Geef het getal in: ' ) )
    if getal < kleinste:
        kleinste = getal
    if getal > grootste:
        grootste = getal
    som += getal

# Weergave
print( "Het grootste getal was:", grootste )
print( "Het kleinste getal was:", kleinste )
print( "Het gemiddelde van de getallen is:", round( som / 10, 1 ) )
