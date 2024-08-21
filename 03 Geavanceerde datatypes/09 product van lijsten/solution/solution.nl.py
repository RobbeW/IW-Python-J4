def lijstproduct(lijst1, lijst2):
    n = len(lijst1)
    nieuw = []
    for i in range(n):
        nieuw.append( lijst1[i]*lijst2[i])
    
    return nieuw
