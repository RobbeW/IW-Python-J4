def opbrengst( lijst, aantal ):
    n = len(lijst)
    nieuw = [ ]
    for i in range(n - aantal + 1):
        if len(nieuw) == 0:
            waarde = 0
            for j in range(aantal):
                waarde += lijst[j]
        else:
            waarde = nieuw[ i - 1 ] + lijst[ i + aantal - 1 ] - lijst[ i - 1]
        nieuw.append( waarde)
    
    return nieuw
