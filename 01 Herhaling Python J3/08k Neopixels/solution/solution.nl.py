# Vraag naar de eAQI
aqi = int(input("Geef de AQI waarde: "))

# Bepaal de hulpvariabelen
if aqi == 1:
    kleur = "Darkgreen"
elif aqi == 2:
    kleur = "Lawngreen"
elif aqi == 3:
    kleur = "Yellow"
elif aqi == 4:
    kleur = "Orange"
elif aqi == 5:
    kleur = "Orangered"
else:
    kleur = "Red"

if aqi == 6:
    aqi = 8

# Weergave op het scherm
for i in range(8):
    if 8 - i <= aqi:
        print(kleur)
    else:
        print("x")
