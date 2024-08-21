def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def vorige_priem(getal):
    getal -= 1
    while not is_priem(getal):
        getal -= 1
    return getal

def volgende_priem(getal):
    getal += 1
    while not is_priem(getal):
        getal += 1
    return getal

# invoer vragen
n = int( input( "Geef een volgnummer in: " ) )

# evenwichtige priemgetallen afdrukken
i = 2
aantal = 0
while aantal != n:
    i += 1
    if is_priem(i):
        if (vorige_priem(i) + volgende_priem(i)) == 2*i:
            aantal += 1

print(i, "is het", n, "e evenwichtige priemgetal.")
