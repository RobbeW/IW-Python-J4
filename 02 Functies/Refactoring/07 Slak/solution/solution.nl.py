def berekenDuur(diepte):
    dag = 0
    hoogte = 0

    # Lus
    while hoogte + 20 < d:
        dag += 1
        hoogte += 20
        hoogte *= 5/6
    dag += 1

    return dag

# Vraagt naar de diepte
d = int( input( "Geef de diepte in: " ) )
dag = berekenDuur(d)
# Eindweergave
if dag == 1:
    print( "Het duurt één dag om uit een put met diepte", d,"cm te klimmen." )
else:
    print( "Het duurt", dag, "dagen om uit een put met diepte", d,"cm te klimmen." )
