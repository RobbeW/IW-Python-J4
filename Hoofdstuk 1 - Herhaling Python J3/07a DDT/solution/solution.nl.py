# Gegevens vragen
dosis = float( input( 'Geef de hoeveelheid in (in mg/kg): ' ) )
grens = 0.01

# Berekening
aantal = 0
while dosis >= grens:
    dosis /= 2
    aantal += 1

# Finale berekening
if aantal == 0:
    print("De grondstaal voldoet al aan de Europese norm.")
else:
    print("Het duurt nog", aantal * 15, "jaar om een veilige dosering van", round(dosis, 4),"mg/kg te bereiken.")
