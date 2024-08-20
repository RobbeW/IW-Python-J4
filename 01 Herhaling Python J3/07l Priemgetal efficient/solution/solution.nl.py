# Een getal vragen
getal = int( input( "Geef een getal in: " ) )

# Controleren of het priem is, met een while lus
i = 2
while i < getal and getal % i != 0:
    i += 1
print()
# Weergave
if i == getal:
    print(getal, "is priem.")
else:
    print(getal, "is niet priem.")
