# Gegevens vragen
aantal = int( input( 'Geef het startaantal in: ' ) )
min = int( input( 'Hoeveel minuten zijn verstreken? ' ) )

# Berekening
aantal_temp = aantal
cycli = min // 20
for i in range(cycli):
    aantal_temp *= 2
    print("Na", (i+1) * 20, "minuten zijn er", aantal_temp, "bacteriën.")

# Finale berekening
perc = int(round(aantal_temp / aantal * 100))
print("Het aantal is toegenomen met ongeveer", str(perc) + "%.")
