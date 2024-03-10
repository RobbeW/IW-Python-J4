def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

# invoer vragen
bovengrens = int( input( "Geef een bovengrens in: " ) )

# priemtweelingen afdrukken
for i in range(2, bovengrens):
    if is_priem(i) and is_priem(i+2) and i+2 < bovengrens:
        print(i, "en", i+2, "zijn priemtweelingen.")