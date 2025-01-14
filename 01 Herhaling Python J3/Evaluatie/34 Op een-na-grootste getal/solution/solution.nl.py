getal1 = int(input("Geef een geheel getal in: "))
getal = int(input("Geef een geheel getal in: "))

if getal < getal1:
    tweede_hoogste = getal
    hoogste = getal1
else:
    tweede_hoogste = getal1
    hoogste = getal

while getal != 0:
    getal = int(input("Geef een geheel getal in: "))
    if getal > hoogste:
        tweede_hoogste = hoogste
        hoogste = getal
    elif getal > tweede_hoogste:
        tweede_hoogste = getal

# Weergave
print("Het op een-na-grootste getal is", tweede_hoogste)
