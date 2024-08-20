# Gegevens vragen
getal = int( input( 'Geef het getal in: ' ) )

# Getalsom berekenen
som = 0
while getal > 0:
    som += getal % 10
    getal //= 10

# En weergeven
print(f"De getalsom is {som}.")
