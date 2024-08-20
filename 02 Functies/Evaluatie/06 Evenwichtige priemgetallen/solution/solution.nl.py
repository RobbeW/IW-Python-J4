def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

def vorige_priem(getal):
    flag = True
    while flag:
        getal -= 1
        flag = not is_priem(getal)
    return getal

def volgende_priem(getal):
    flag = True
    while flag:
        getal += 1
        flag = not is_priem(getal)
    return getal

# invoer vragen
n = int( input( "Geef een volgnummer in: " ) )

# priemtweelingen afdrukken
i = 2
aantal = 0
while aantal != n:
    i += 1
    if is_priem(i):
        if (vorige_priem(i) + volgende_priem(i)) == 2*i:
            aantal += 1

print(i, "is het", n, "e evenwichtige priemgetal.")
