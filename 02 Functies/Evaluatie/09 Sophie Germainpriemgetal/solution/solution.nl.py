def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def is_germainpriem(getal):
    return is_priem(getal) and is_priem(2 * getal + 1)

# Invoer vragen
getal = int(input( "Geef een getal in: " ) )

# Uitvoer
if is_germainpriem(getal):
    print(f"Dit is een Sophie Germainpriemgetal, het veilige priemgetal is {2 * getal + 1}")
else:
    print("Dit is geen Sophie Germainpriemgetal")
