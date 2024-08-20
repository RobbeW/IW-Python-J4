# Gegevens vragen
getal = int( input( 'Geef een getal in: ' ) )

# Berekening
i = 1
while True:
    test = getal - i
    is_priem = True
    for j in range(2, test):
        if test % j == 0:
            is_priem = False
    
    if is_priem:
        break
    i += 1

print(f"Het grootste priemgetal kleiner dan {getal} is {test}.")
