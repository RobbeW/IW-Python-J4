def verblijf1(aantal):
    kost = 55 * aantal
    if aantal >= 5:
        kost *= 0.6
    elif aantal >= 4:
        kost *= 0.8
    elif aantal >= 3:
        kost *= 0.9
    return kost

def verblijf2(aantal):
    kost = 49.95 * aantal
    if aantal >= 6:
        kost = (aantal - 2) * 49.95
    elif aantal >= 4:
        kost = (aantal - 1) * 49.95
    return kost

# Aantal reizigers
aantal = int( input( 'Geef het aantal reizigers in: ' ) )

# Berekening van de kostprijzen:
totaal1 = verblijf1(aantal)
totaal2 = verblijf2(aantal)

# Weergave van de mededeling
print("Verblijf 1 kost: €", round( totaal1, 2 ) )
print("Verblijf 2 kost: €", round( totaal2, 2 ) )

if totaal1 < totaal2:
    print("Verblijf 1 is goedkoper.")
else:
    print("Verblijf 2 is goedkoper.")
