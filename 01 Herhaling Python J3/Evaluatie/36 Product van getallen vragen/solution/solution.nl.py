getal = int(input("Geef een getal in (0 om te stoppen): "))
aantal = 0
product = getal

while getal != 0:
    aantal += 1
    product *= getal
    
    getal = int(input("Geef een getal in (0 om te stoppen): "))

# Weergave
if aantal == 0:
    print("Er werd geen enkel getal ingevoerd.")
elif aantal == 1:
    print("Enkel het getal", product, "werd ingevoerd." )
else:
    print(product, "is het product van deze", aantal, "getallen.")
