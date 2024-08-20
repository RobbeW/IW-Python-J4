# Vraagt naar de coefficienten
a = float( input( "Geef a in: " ) )
b = float( input( "Geef b in: " ) )
c = float( input( "Geef c in: " ) )

# Weergave
if a == 0:
    print( 'Dit is geen vkv!' )
else:
    if b == 0 or c == 0:
        print( 'Deze vkv is onvolledig.' )
    else:
        print( 'Deze vkv is volledig.' )
