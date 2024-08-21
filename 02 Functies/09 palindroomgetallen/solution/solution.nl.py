def is_palindroom( getal ):
    oorspronkelijke = getal
    nieuw = getal % 10
    getal //= 10
    
    while getal != 0:
        eenheden = getal % 10
        getal //= 10
        nieuw = nieuw * 10 + eenheden
    
    return nieuw == oorspronkelijke

# Invoer vragen
a = int( input( "Geef een ondergrens in: " ) )
b = int( input( "Geef een bovengrens in: " ) )

# Bepalen van de palindroomgetallen
aantal = 0
for getal in range(a + 1, b):
    if is_palindroom(getal):
        print(getal, "is een palindroomgetal.")
        aantal += 1

# Uiteindelijke afdruk
if aantal == 1:
    print("Er was slechts één palindroomgetal.")
elif aantal == 0:
    print("Er werden geen palindroomgetallen gevonden.")
else:
    print("Er waren", aantal, "palindroomgetallen.")
