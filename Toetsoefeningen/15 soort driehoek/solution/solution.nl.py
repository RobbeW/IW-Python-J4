# Vraag naar de zijden
a = float( input( "Voer de lengte van de eerste zijde in: " ) )
b = float( input( "Voer de lengte van de tweede zijde in: " ) )
c = float( input( "Voer de lengte van de derde zijde in: " ) )

# Bepalen van de langste zijde
x = max( a, b, c )
y = min( a, b, c )
z = a + b + c - ( x + y )

# Weergave op het scherm
if x**2 < y**2 + z**2:
    print("De driehoek is scherphoekig.")
elif x**2 > y**2 + z**2:
    print("De driehoek is stomphoekig.")
else:
    print("De driehoek is rechthoekig.")
