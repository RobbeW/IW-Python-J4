import math
grootte = int(input("Geef de bestandsgrootte in: "))

clusters = math.ceil(grootte / 4096)
eff = round(grootte / (clusters * 4096) * 100, 1)

print(f"Er zijn {clusters} clusters nodig. Dit is {eff} % efficiënt.")
