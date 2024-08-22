def harmonisch_gemiddelde( lijst ):
    n = len(lijst)
    som = 0
    for getal in lijst:
        som += 1/getal
    return round( n / som, 3 )
