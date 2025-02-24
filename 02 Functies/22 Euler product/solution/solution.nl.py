import math

def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def benadering_euler(aantal_factoren):
    product = 1
    aantal = 0
    i = 2
    while aantal < aantal_factoren:
        factor = i**2 / (i**2 - 1)
        if is_priem(i):
            product *= factor
            aantal += 1
        i += 1
    
    return round(product, 6)


aantal = int(input("Geef het aantal factoren in: "))
benadering = benadering_euler(aantal)
benadering = math.sqrt(6 * benadering)

if aantal == 1:
    print("De benadering van pi met 1 factor is:", round(benadering, 4))
else:
    print("De benadering van pi met", aantal, "factoren is:", round(benadering, 4))