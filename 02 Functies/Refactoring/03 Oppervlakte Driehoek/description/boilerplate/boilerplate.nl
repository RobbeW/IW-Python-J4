basis = float(input("Hoe lang is de basis van jouw driehoek in cm: "))
hoogte = float(input("Hoe lang is de hoogte van jouw driehoek in cm: "))
opp = round(basis * hoogte / 2, 2)
print("De oppervlakte van een driehoek met basis", basis, "cm en hoogte", hoogte, "cm is", opp, "cm².")