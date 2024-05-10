def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

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
