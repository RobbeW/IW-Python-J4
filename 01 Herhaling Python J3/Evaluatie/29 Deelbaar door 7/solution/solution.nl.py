# Invoer
getal = int(input("Geef het getal in: "))
i = 0

while getal // 100 > 0:
    i += 1
    deel2 = getal % 10
    deel1 = getal // 10
    getal = deel1 - 2 * deel2
    print(f"{i}e stap: Het verschil van {deel1} en {2 * deel2} is {getal}")
