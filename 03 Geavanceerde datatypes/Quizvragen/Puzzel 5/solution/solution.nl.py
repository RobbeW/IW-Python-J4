def slaapplaats(lijst):
    # Controleer vooraan
    teller = 0
    while lijst[teller] != "X":
        teller += 1
    hoogste = 2 * teller - 1

    # Controleer achteraan
    teller = 0
    while lijst[len(lijst) - 1 - teller] != "X":
        teller += 1
    teller = 2 * teller - 1
    if teller > hoogste:
        hoogste = teller

    # Controleer in het midden
    teller = 0
    for i in range(len(lijst)):
        if lijst[i] == "X":
            if teller > hoogste:
                hoogste = teller
            teller = 0
        else:
            teller += 1

    return (hoogste - 1) // 2