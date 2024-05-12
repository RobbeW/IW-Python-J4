def olympisch_gemiddelde( lijst ):
    n = len(lijst)
    som = 0
    for getal in lijst:
        som += getal
    som = som - min(lijst) - max(lijst)
    return round(som / (n - 2), 2)
