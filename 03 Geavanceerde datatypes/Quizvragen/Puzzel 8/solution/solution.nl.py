def aantal_cijfers(getal):
    teller = 0
    while getal > 0:
        teller += 1
        getal //= 10
    return teller