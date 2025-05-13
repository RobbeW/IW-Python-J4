def negatieve_lijst(lijst):   
    nieuw = []

    for getal in lijst:
        if getal <= 0:
            nieuw.append(getal)

    return nieuw
