# Gegevens aan de gebruiker vrage
lichtstroom = float( input( "Geef de lichtstroom in: " ) )
energieverbruik = float( input( "Geef het energieverbruik in: " ) )

# Berekenen van de efficientie
efficientie = lichtstroom / energieverbruik

# Label bepalen
if efficientie >= 210:
    label = 'A'
elif efficientie >= 185:
    label = 'B'
elif efficientie >= 160:
    label = 'C'
elif efficientie >= 135:
    label = 'D'
elif efficientie >= 110:
    label = 'E'
elif efficientie >= 85:
    label = 'F'
else:
    label = 'G'

# Weergave
print('Energieklasse:', label)
