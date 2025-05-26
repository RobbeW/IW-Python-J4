def aantal_negatieve(lijst):   
    aantal = 0

    for getal in lijst:
        if getal <= 0:
            aantal += 1

    return aantal
