getal = int(input("Geef een getal in (strikt negatief om te stoppen): "))
aantal = 1

while getal >= 0:
    getal = int(input("Geef een getal in (strikt negatief om te stoppen): "))
    aantal += 1

if aantal - 1 == 1:
    print("Je tikte één positief getal in.")
else:
    print("Je tikte", aantal - 1, "positieve getallen in.")
