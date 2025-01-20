def discriminant(a, b, c):
    D = b**2 - 4 * a * c
        
    return D

def aantal_oplossingen(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        return 0
    elif D > 0:
        return 2
    else:
        return 1


# Invoer vragen
a = int(input("Geef de coëfficiënt van x² in: "))
b = int(input("Geef de coëfficiënt van x in: "))
c = int(input("Geef de constante in: "))

print()
aantal = aantal_oplossingen(a, b, c)
if aantal < 0:
    print("Er zijn geen reële oplossingen.")
elif aantal == 2:
    print("Er zijn twee verschillende reële oplossingen.")
else:
    print("Er is exact één reële oplossing.")

