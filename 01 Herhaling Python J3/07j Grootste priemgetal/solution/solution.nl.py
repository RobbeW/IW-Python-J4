# Gegevens vragen
getal = int( input( 'Geef een getal in: ' ) )

# Berekening
i = 1
is_priem = False
while not is_priem:
    test = getal - i
    
    j = 2
    while j < test and test % j != 0:
        j += 1
    
    if j != test:
        i += 1
    else:
        is_priem = True

print(f"Het grootste priemgetal kleiner dan {getal} is {test}.")
