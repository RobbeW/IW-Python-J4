def somlijst( lijst ):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        som = 0
        for j in range(i+1):
            som += lijst[j]
        
        nieuw.append( som )
    
    return nieuw
