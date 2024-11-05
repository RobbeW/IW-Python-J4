import math
# Vraagt naar de coefficienten
a = float( input( "Geef a in: " ) )
b = float( input( "Geef b in: " ) )
c = float( input( "Geef c in: " ) )

# Weergave
if a * c < 0:
    print("Deze vkv kan niet meteen naar een kwadraat herleid worden.")
else:
    if 2 * math.sqrt(a*c) == abs(b):
        print("Deze vkv kan meteen naar een kwadraat herleid worden.")
    else:
        print("Deze vkv kan niet meteen naar een kwadraat herleid worden.")
