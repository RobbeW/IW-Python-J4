import math
def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem

def telpriem( x ):
    x = math.floor(x)
    aantal = 0
    for getal in range(2, x+1):
        if is_priem(getal):
            aantal += 1
    return aantal

x = float( input( "Geef een strikt positief getal in: " ) )
aantal = telpriem( x )
if aantal == 1:
    print(f"Er is {aantal} priemgetal kleiner dan of gelijk aan {x}")
else:
    print(f"Er zijn {aantal} priemgetallen kleiner dan of gelijk aan {x}")
