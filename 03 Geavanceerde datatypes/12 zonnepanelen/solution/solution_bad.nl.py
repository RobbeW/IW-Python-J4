def opbrengst( lijst, aantal ):
    n = len(lijst)
    nieuw = [ ]
    for i in range(n - aantal+1):
        waarde = 0
        for j in range(i, i + aantal):
            waarde += lijst[j]

        nieuw.append( waarde)
    
    return nieuw
