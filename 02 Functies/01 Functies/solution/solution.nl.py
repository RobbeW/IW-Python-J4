def oppervlakte_driehoek(basis , hoogte):
    opp = 0.5 * basis * hoogte
    return opp

b = 4.5
h = 1.0
opp = oppervlakte_driehoek(b, h)
print("Een driehoek met basis", b, "cm en hoogte", h, "cm heeft oppervlakte", opp, "cm².")
