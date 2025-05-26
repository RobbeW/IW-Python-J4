def hoogtemeters(hoogtes):   
    hoogte = 0

    for i in range(len(hoogtes) - 1):
        if hoogtes[i+1] > hoogtes[i]:
            hoogte += hoogtes[i+1] - hoogtes[i]
            
    return hoogte
