# Temperatuur
temp = float( input( 'Geef de starttemperatuur in: ' ) )

# Berekening van de temperaturen:
height = 1900
if temp > 20:
    temp += 0.65
else:
    print("Het is voor Laura te koud te beginnen met de klim.")

while temp > 20 and height <= 2900:
    temp -= 0.65
    if temp > 20:
        print("Op een hoogte van", height, "m meet de temperatuur", round(temp, 1), "°C.")
        height += 100
    else: 
        print("Laura, stop met klimmen op", height, "m.")
