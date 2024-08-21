def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

# invoer vragen
n = int( input( "Geef een volgnummer in: " ) )

# priemtweelingen afdrukken
getal = 2
i = 2
aantal = 0
while aantal != n:
    i += 1
    if is_priem(i):
        verschil = i - getal
        getal = i
        aantal += 1

print("Het", n, "e priemgetalhiaat is", verschil)
