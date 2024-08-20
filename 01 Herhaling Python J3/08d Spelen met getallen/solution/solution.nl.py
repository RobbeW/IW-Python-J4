# Invoer vragen
a = int(input("Geef het eerste getal in: "))
b = int(input("Geef het tweede getal in: "))
c = int(input("Geef het derde getal in: "))

# Uitvoer maken
if a + b == c or a * b == c or abs(a - b) == c or a / b == c or b / a == c:
    print("Mogelijk")
else:
    print("Onmogelijk")
