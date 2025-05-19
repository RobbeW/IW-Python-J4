def bas_aanpassen(niveaus, aanpassingen):
    n = len(niveaus)
    nieuw = []
    for i in range(n):
        nieuw.append(niveaus[i] + aanpassingen[i])
    return nieuw
