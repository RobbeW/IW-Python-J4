def berekenToename(aantal, min):
    # Berekening
    aantal_temp = aantal
    cycli = min // 20
    for i in range(cycli):
        aantal_temp *= 2
        print("Na", (i+1) * 20, "minuten zijn er", aantal_temp, "bacteriën.")
    return aantal_temp / aantal


# Gegevens vragen
aantal = int( input( 'Geef het startaantal in: ' ) )
min = int( input( 'Hoeveel minuten zijn verstreken? ' ) )

toename = berekenToename(aantal, min)
print("Het startaantal werd met", toename, "vermenigvuldigd!")
