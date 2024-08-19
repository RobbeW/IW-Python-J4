# Invoer van een aantal seconden
uur = int(input("Geef het uur in: "))
minuten = int(input("Geef de minuten in: "))
extra = int(input("Geef de extra minuten in: "))

# Berekeningen
minuten = minuten + extra
uur = (uur + minuten // 60) % 24

# Uitvoer
print(f"{uur} : {minuten % 60}")
