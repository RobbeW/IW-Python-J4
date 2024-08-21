def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

# invoer vragen
bovengrens = int( input( "Geef een bovengrens in: " ) )

# priemtweelingen afdrukken
aantal = 0
for i in range(2, bovengrens-6):
    if is_priem(i) and is_priem(i+6):
        aantal += 1
        print(i, "en", i+6, "zijn sexy priemgetallen.")

if aantal == 0:
    print("Er werden geen sexy priemgetallen kleiner dan", bovengrens, "gevonden.")
