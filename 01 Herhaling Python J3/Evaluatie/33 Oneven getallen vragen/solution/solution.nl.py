getal = int(input("Geef een getal in (-1 om te stoppen): "))

aantal = 0
while getal != -1:
    if getal % 2 == 1:
        aantal += 1
    
    getal = int(input("Geef een getal in (-1 om te stoppen): "))

# Weergave
if aantal == 0:
    print("Er waren geen oneven getallen.")
elif aantal == 1:
    print("Er was één oneven getal.")
else:
    print("Er waren", aantal, "oneven getallen.")
