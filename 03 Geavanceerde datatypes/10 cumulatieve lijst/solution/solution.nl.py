def somlijst( lijst ):
    n = len(lijst)
    nieuw = [ lijst[0] ]
    for i in range(1, n):
        waarde = nieuw[ i - 1 ] + lijst[ i ]
        nieuw.append( waarde)
    
    return nieuw
