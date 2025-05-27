def vrije_ruimte_links( lijst ):
    n = len(lijst)
    aantal = 0
    nieuw = []
    for i in range(n):
        nieuw.append(aantal)
        if lijst[i] == " ":
            aantal += 1
        else:
            aantal = 0
    
    return nieuw
