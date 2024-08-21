def score(w1, w2):
    if w1 + w2 == 3:
        score = 1000
    elif w1 == w2:
        score = w1 * 100
    else:
        score = max(w1, w2) * 10 + min(w1, w2)

    return score

def mexen(s0, s1, t0, t1):
    p1 = score(s0, s1)
    p2 = score(t0, t1)
    
    if p1 > p2:
        tekst = "speler 1"
    elif p1 < p2:
        tekst = "speler 2"
    else:
        tekst = "gelijkspel"
    
    return tekst
