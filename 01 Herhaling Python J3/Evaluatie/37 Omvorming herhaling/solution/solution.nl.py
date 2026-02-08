bedrag = float(input("Wat is het startbedrag?"))
interest = float(input("Hoeveel interest krijgt Jos per trimester (3 maand)?"))
i = 3

while i < 37:
    bedrag += bedrag * interest / 100
    print("Na", i // 12, "jaar en", i % 12, "maand heeft Jos €", round(bedrag, 2), "op zijn rekening staan.")
    i += 3