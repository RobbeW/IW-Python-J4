def gevoelstemperatuur(T, W):
    G = 13.12 + 0.6215 * T  + (0.3965 * T - 11.37) * (3.6 * W)**0.16
        
    return round(G, 2)


def beaufort_naar_km_u(B):
    v = 0.8360 * B**(3 / 2)
    W = v * 3.6
    return round(W, 6)

def gevoelstemperatuur_beaufort(T, B):
    W = beaufort_naar_km_u(B)
    G = gevoelstemperatuur(T, W)
        
    return round(G, 2)

# Invoer vragen
T = float(input("Geef de gevoelstemperatuur in (in °C): "))
W = float(input("Geef de windsnelheid in: "))
eenheid = input("Geef de eenheid van de windsnelheid in (km/u of B): ")

if eenheid == "B":
    G = gevoelstemperatuur_beaufort(T, W)
else:
    G = gevoelstemperatuur(T, W)

print()
print("De temperatuur voelt aan als", G, "°C.")
