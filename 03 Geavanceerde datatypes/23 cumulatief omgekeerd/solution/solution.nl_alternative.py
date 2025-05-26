def draai_om(lijst):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        nieuw.append(lijst[n - i - 1])
    return nieuw

def somlijst_omgekeerd( lijst ):
    n = len(lijst)
    som = 0
    nieuw = []
    for i in range(n):
        som += lijst[n - i - 1]
        nieuw.append(som)
    
    return draai_om(nieuw)
