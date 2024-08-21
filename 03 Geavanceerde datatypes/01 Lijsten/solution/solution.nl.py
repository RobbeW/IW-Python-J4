def verwissel( lijst ):
    # Haal het eerste en laatste element op
    n = len(lijst)
    eerste = lijst[0]
    laatste = lijst[n - 1]

    # Wissel deze om
    lijst[0] = laatste
    lijst[n - 1] = eerste

    return lijst
