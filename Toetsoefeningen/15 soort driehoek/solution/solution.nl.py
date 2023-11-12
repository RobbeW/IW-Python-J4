# Vraag naar de zijden
a = float( input( "Voer de lengte van de eerste zijde in: " ) )
b = float( input( "Voer de lengte van de tweede zijde in: " ) )
c = float( input( "Voer de lengte van de derde zijde in: " ) )

# Bepalen van de langste zijde
if a > b and a > c:
    x = a
    y = b
    z = c
elif b > a and b > c:
    x = b
    y = a
    z = c
else:
    x = c
    y = a
    z = b

# Weergave op het scherm
if x**2 < y**2 + z**2:
    print("De driehoek is scherphoekig.")
elif x**2 > y**2 + z**2:
    print("De driehoek is stomphoekig.")
else:
    print("De driehoek is rechthoekig.")
