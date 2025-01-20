def berekenHoek(start, eind):
    hoek = eind - start
    if hoek <= -180:
        hoek = 360 + hoek
    if hoek > 180:
        hoek -= 360
    return hoek

# Vraag naar het aantal hapjes
start = int(input("Geef de startpositie in: "))
eind = int(input("Geef de eindpositie in: "))

# Weergave
print(berekenHoek(start, eind))
