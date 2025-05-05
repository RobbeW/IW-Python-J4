def verwissel(lijst, nummer1, nummer2):   
    eerste = lijst[nummer1 - 1]
    tweede = lijst[nummer2 - 1]

    # Wissel deze om
    lijst[nummer1 - 1] = tweede
    lijst[nummer2 - 1] = eerste

    return lijst
