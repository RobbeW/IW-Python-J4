def linkersom(lijst):   
    n = len(lijst)
    nieuw = []
    som = 0
    for i in range(n):
        nieuw.append(som)
        som += lijst[i]
            
    return nieuw

def draai_om(lijst):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        nieuw.append(lijst[n - i - 1])
    return nieuw

def rechtersom(lijst):   
    omgekeerd = draai_om(lijst)
    nieuw = linkersom(omgekeerd)
    nieuw = draai_om(nieuw)
            
    return nieuw

def links_rechts_verschil(lijst):
    n = len(lijst)
    links = linkersom(lijst)
    rechts = rechtersom(lijst)
    
    nieuw = []
    for i in range(n):
        nieuw.append( abs(links[i] - rechts[i]))
    return nieuw