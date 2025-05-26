def draai_om(lijst):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        nieuw.append(lijst[n - i - 1])
    return nieuw

def somlijst( lijst ):
    n = len(lijst)
    nieuw = [ lijst[0] ]
    for i in range(1, n):
        waarde = nieuw[ i - 1 ] + lijst[ i ]
        nieuw.append( waarde)
    
    return nieuw

def somlijst_omgekeerd( lijst ):
    lijst = draai_om(lijst)
    nieuw = somlijst(lijst)
    nieuw = draai_om(nieuw)
    
    return nieuw
