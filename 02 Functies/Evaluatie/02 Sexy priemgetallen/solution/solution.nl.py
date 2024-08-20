def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

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
