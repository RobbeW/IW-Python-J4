# Temperatuur
temp = float( input( 'Geef de starttemperatuur in: ' ) )

# Berekening van de temperaturen:
temp += 0.65
for h in range( 1900, 3000, 100 ):
    temp -= 0.65
    print("Op een hoogte van", h, "m meet de temperatuur", str(round(temp, 1))+"°C.")    
