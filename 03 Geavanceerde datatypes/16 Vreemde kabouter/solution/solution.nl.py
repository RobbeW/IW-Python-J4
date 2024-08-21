def koning(nummers):
    i = 1
    while nummers[i] == nummers[i - 1] + 1:
        i += 1
    return i
