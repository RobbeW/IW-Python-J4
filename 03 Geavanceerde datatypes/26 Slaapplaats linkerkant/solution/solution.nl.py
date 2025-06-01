def aantal_links(bedden):
    n = len(bedden)
    nieuw = []
    waarde = -1
    for i in range(n):
        if bedden[i] == "X":
            waarde = 0
        elif bedden[i] == "." and waarde != -1:
            waarde += 1
        nieuw.append(waarde)
    
    return nieuw
