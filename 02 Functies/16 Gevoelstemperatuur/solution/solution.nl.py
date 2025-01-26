def gevoelstemperatuur(T, W):
    G = 13.12 + 0.6215 * T  + (0.3965 * T - 11.37) * (3.6 * W)**0.16
        
    return round(G, 2)


# Invoer vragen
T = float(input("Geef de gevoelstemperatuur in (in °C): "))
W = float(input("Geef de windsnelheid in (in km/u): "))

G = gevoelstemperatuur(T, W)
print("De temperatuur voelt aan als", G, "°C.")
