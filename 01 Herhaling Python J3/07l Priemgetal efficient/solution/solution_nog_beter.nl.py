import math
# Een getal vragen
getal = int( input( "Geef een getal in: " ) )
bovengrens = math.ceil(math.sqrt(getal))

# Controleren of het priem is, met een while lus
i = 2
while i < bovengrens and getal % i != 0:
    i += 1

# Weergave
if i == bovengrens:
    print(getal, "is priem.")
else:
    print(getal, "is niet priem.")
