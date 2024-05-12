def verwissel( lijst ):
    # Haal het eerste en laatste element op
    n = len(lijst)
    eerste = lijst[0]
    laatste = lijst[n]

    # Wissel deze om
    lijst[0] = laatste
    lijst[n] = eerste

    return lijst
