def elisabeth_wedstrijd(punten):
    n = len(punten)
    som = 0
    for punt in punten:
        som += punt
    
    nieuwe_punten = []
    for punt in punten:
        gemiddelde_rest = (som - punt) / (n - 1)
        if punt / gemiddelde_rest > 1.2:
            nieuwe_punten.append(gemiddelde_rest * 1.2)
        elif punt / gemiddelde_rest < 0.8:
            nieuwe_punten.append(gemiddelde_rest * 0.8)
        else:
            nieuwe_punten.append(punt)
    
    som = 0
    for punt in nieuwe_punten:
        som += punt
    
    return round(som / n, 2)
