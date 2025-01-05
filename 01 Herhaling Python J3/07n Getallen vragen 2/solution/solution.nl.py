aantal = 0
while True:
    getal = int(input("Geef een getal in (strikt negatief om te stoppen): "))
    if getal < 0:
        break
    aantal += 1

if aantal == 1:
    print("Je tikte één positief getal in.")
else:
    print("Je tikte", aantal, "positieve getallen in.")
