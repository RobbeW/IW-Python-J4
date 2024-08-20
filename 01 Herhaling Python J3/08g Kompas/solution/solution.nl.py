# Vraag naar het aantal hapjes
start = int(input("Geef de startpositie in: "))
eind = int(input("Geef de eindpositie in: "))

# Bepalen van de hoek
hoek = eind - start
# Aanpassen indien buiten de grenzen
if hoek <= -180:
    hoek = 360 + hoek
if hoek > 180:
    hoek -= 360

# Weergave
print(hoek)
