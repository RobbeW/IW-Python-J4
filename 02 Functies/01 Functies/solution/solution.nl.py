def oppervlakte_driehoek(basis , hoogte):
    opp = 0.5 * basis * hoogte
    return opp

basis = 4.5
hoogte = 1.0
opp = oppervlakte_driehoek(basis, hoogte)
print("Een driehoek met basis", basis, "cm en hoogte", hoogte, "cm heeft oppervlakte", opp, "cm².")
