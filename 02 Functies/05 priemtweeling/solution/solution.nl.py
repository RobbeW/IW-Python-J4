def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

# invoer vragen
bovengrens = int( input( "Geef een bovengrens in: " ) )

# priemtweelingen afdrukken
for i in range(2, bovengrens):
    if is_priem(i) and is_priem(i+2) and i+2 < bovengrens:
        print(i, "en", i+2, "zijn priemtweelingen.")
