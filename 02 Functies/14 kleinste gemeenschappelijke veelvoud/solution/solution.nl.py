def kgv(getal1, getal2):
    veelvoud1 = getal1
    veelvoud2 = getal2
    while veelvoud1 != veelvoud2:
        if veelvoud1 < veelvoud2:
            veelvoud1 += getal1
        else:
            veelvoud2 += getal2
        
    return veelvoud1


# Invoer vragen
a = int(input("Geef het eerste getal in: "))
b = int(input("Geef het tweede getal in: "))

print("Het kgv van", a, "en", b, "is", kgv(a, b))
