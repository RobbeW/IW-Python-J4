# Gegevens vragen
getal = int( input( 'Geef een getal in: ' ) )

# Berekening
voorwaarde = True
i = 1
while voorwaarde:
    test = getal - i
    niet_priem = 0
    for j in range(2, test):
        if test % j == 0:
            niet_priem = 1
    
    if niet_priem == 0:
        voorwaarde = False
    i += 1

print("Het grootste priemgetal kleiner dan", getal, "is", str(test)+"." )
