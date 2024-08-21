import math

def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def telpriem(x):
    x = math.floor(x)
    aantal = 0
    for getal in range(2, x + 1):
        if is_priem(getal):
            aantal += 1
    return aantal

x = float( input( "Geef een strikt positief getal in: " ) )
aantal = telpriem( x )
if aantal == 1:
    print(f"Er is {aantal} priemgetal kleiner dan of gelijk aan {x}")
else:
    print(f"Er zijn {aantal} priemgetallen kleiner dan of gelijk aan {x}")
