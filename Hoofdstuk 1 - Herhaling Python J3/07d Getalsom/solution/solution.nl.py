# Gegevens vragen
getal = int( input( 'Geef de starttemperatuur in: ' ) )

# Getalsom berekenen
som = 0
while getal > 0:
    som += getal % 10
    getal //= 10

# En weergeven
print()
print( "De getalsom is", str(som) + "." )