def draai_om(lijst):
    n = len(lijst)
    nieuw = []
    for i in range(n):
        nieuw.append(lijst[n - i - 1])
    return nieuw
