# Invoer
getal = int(input("Geef het getal in: "))

# Berekening
som_even = 0
som_oneven = 0
i = 0

voorwaarde = True
while voorwaarde:
    i += 1
    cijfer = getal % 10
    getal = getal // 10
    if i % 2 == 0:
        som_even += cijfer
    else:
        som_oneven += cijfer
    
    if getal == 0:
        voorwaarde = False

# Weergave
print()
print("De som van de getallen op de oneven rang is:", som_oneven)
print("De som van de getallen op de even rang is:", som_even)
if (som_even - som_oneven) % 11 == 0:
    print("Dit getal is deelbaar door 11!")
else:
    print("Dit getal is NIET deelbaar door 11!")
