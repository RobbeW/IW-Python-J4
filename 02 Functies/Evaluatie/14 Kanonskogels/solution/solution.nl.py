def piramidegetal(n):
    som = 0
    for i in range(n):
        som += (i + 1)**2
    return som

def zijde_kanon(aantal):
    zijde = 1
    while piramidegetal(zijde) <= aantal:
        zijde += 1
    
    return zijde -1
    

n = int(input("Geef het aantal kanonskogels in: "))

antwoord = zijde_kanon(n)

print()
if antwoord > 1:
    print("Plaats", antwoord, "kanonskogels naast elkaar als zijde van het eerste vierkant.")
else:
    print("Deze ene kanonskogel kan je meteen rangschikken als een piramide.")
