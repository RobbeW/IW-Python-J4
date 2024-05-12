def verwissel( lijst ):
    n = len(lijst)
    eerste = lijst[0]
    laatste = lijst[n-1]
    lijst[0] = laatste
    lijst[n-1] = eerste
    return lijst