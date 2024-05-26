def somlijst( lijst ):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        som = 0
        for j in range(i):
            som += lijst[j]
        
        nieuw.append( som )
    
    return nieuw

print( somlijst( [1, 5, 6, -2, 0, 5, 9] ))