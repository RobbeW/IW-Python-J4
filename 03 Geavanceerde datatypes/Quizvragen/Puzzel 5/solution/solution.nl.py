def slaapplaats(lijst):
    teller = 0
    while lijst[teller] != "X":
        teller += 1
    hoogste = 2 * teller - 1
    for i in range(teller, len(lijst)):
        if lijst[i] == "X":
            if teller > hoogste:
                hoogste = teller
            teller = 0
        elif i == len(lijst) - 1:
            teller = 2 * teller + 1
            if teller > hoogste:
                hoogste = teller
        else:
            teller += 1

    return (hoogste - 1) // 2