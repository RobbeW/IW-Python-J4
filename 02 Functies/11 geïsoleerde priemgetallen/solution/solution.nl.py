def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

# invoer vragen
bovengrens = int( input( "Geef een bovengrens in: " ) )

# priemtweelingen afdrukken
for i in range(2, bovengrens+1):
    if i == 2:
        print("2 is een geïsoleerd priemgetal.")
    elif is_priem(i) and not is_priem(i-2)  and not is_priem(i+2) :
        print(i, "is een geïsoleerd priemgetal.")
