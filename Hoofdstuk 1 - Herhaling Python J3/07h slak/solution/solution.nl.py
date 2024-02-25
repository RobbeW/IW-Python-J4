# Vraagt naar de diepte
d = int( input( "Geef de diepte in: " ) )
dag = 0
hoogte = 0

# Lus
flag = True
while flag:
    dag += 1
    hoogte += 20
    flag = hoogte < d 
    hoogte *= 5/6

# Eindweergave
if dag == 1:
    print( "Het duurt één dag om uit een put met diepte", d,"cm te klimmen." )
else:
    print( "Het duurt", dag, "dagen om uit een put met diepte", d,"cm te klimmen." )
