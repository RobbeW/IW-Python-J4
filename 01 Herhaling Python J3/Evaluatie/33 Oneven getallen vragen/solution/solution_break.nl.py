aantal = 0
while True:
    getal = int(input("Geef een getal in (-1 om te stoppen): "))
    if getal == -1:
        break
    if getal % 2 == 1:
        aantal += 1

# Weergave
if aantal == 0:
    print("Er waren geen oneven getallen.")
elif aantal == 1:
    print("Er was één oneven getal.")
else:
    print("Er waren", aantal, "oneven getallen.")
