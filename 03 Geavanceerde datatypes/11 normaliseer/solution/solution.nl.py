def normaliseer( lijst ):
    som = 0
    for getal in lijst:
        som += getal

    nieuw = []
    n = len(lijst)
    for i in range(n):
        nieuw.append( lijst[i] / som )
    
    return nieuw
