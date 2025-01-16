aantal = 0
product = 1
while True:
    getal = int(input("Geef een getal in (0 om te stoppen): "))
    if getal == 0:
        break
    aantal += 1
    product *= getal

# Weergave
if aantal == 0:
    print("Er werd geen enkel getal ingevoerd.")
elif aantal == 1:
    print("Enkel het getal", product, "werd ingevoerd." )
else:
    print(product, "is het product van deze", aantal, "getallen.")
