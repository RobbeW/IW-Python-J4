def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

# Schrijf hieronder je programma
