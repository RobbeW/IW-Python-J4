def is_rechthoekig( getal ):
    result = False
    for i in range(2, getal):
        if i*(i+1) == getal:
            result = True
    return result

# Bovengrens vragen en afdrukken
bovengrens = int( input( "Geef een bovengrens in: " ) )

for i in range(1, bovengrens):
    if is_rechthoekig(i):
        print(i, "is een rechthoekig getal.")
