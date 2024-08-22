def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

def volgende_priem(getal):
    getal += 1
    while not is_priem(getal):
        getal += 1
    return getal
