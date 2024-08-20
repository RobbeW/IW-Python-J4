# Initialisatie
n = int(input("Geef een getal in (eindig met 0): "))
lengte = 1
if n != 0:
    max_lengte = 1
else:
    max_lengte = 0

# Bepaal max deelrij
while n != 0:
    vorige = n
    n = int(input("Geef een getal in (eindig met 0): "))
    if n == vorige:
        lengte += 1
        if lengte > max_lengte:
            max_lengte = lengte
    else:
        lengte = 1

# Uitvoer
print(max_lengte)
