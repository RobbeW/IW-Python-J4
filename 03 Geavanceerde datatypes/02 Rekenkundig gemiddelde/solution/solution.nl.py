def gemiddelde( lijst ):
    n = len(lijst)
    som = 0
    for getal in lijst:
        som += getal
    return round(som / n, 3)
