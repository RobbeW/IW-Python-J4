def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def priemtweeling( getal ):
    resultaat = 0
    if is_priem( getal ):
        if is_priem( getal - 2) and is_priem( getal +2 ):
            resultaat = 2
        elif is_priem( getal - 2) or is_priem( getal + 2):
            resultaat = 1
        else:
            resultaat = 0
    return resultaat

# Invoer vragen
getal = int(input( "Geef een getal in: " ) )

# Uitvoer
aantal = priemtweeling(getal)

if aantal == 2:
    print("Je kan twee priemtweelingen vinden van", getal)
elif aantal == 1:
    print("Je kan één priemtweeling vinden van", getal)
else:
    print("Je kan geen priemtweeling vinden van", getal)
