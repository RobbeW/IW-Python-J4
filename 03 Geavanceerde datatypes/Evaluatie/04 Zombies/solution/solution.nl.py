import math
def aantal_gezond(sectoren):
    n = len(sectoren)
    aantal = 0
    for getal in sectoren:
        if getal == 0:
            aantal += 1
    return aantal


def infectie(sectoren):
    n = len(sectoren)
    nieuw = []
    
    if sectoren[0] == 0:
        nieuw.append(sectoren[1])
    else:
        nieuw.append(sectoren[0])
    
    for i in range(1, n - 1):
        if sectoren[i] == 0:
            gemiddeld = (sectoren[i-1]+sectoren[i+1]) / 2
            nieuw.append(math.floor(gemiddeld))
        else:
            nieuw.append(sectoren[i])
    
    if sectoren[n-1] == 0:
        nieuw.append(sectoren[n-2])
    else:
        nieuw.append(sectoren[n-1])
    
    return nieuw