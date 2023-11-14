import math
# Vraagt naar de coefficienten
a = float( input( "Geef a in: " ) )
b = float( input( "Geef b in: " ) )
c = float( input( "Geef c in: " ) )

# Weergave
if a < 0 and c < 0 or a > 0 and c > 0:
    if 2 * math.sqrt(abs(a)*abs(c)) == abs(b):
        print("Deze vkv kan eenvoudiger geschreven worden.")
    else:
        print("Deze vkv kan niet eenvoudiger geschreven worden.")
else:
    print("Deze vkv kan niet eenvoudiger geschreven worden.")
