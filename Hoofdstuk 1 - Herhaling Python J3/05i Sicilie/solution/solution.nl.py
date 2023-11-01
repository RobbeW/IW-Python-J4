# Aantal reizigers
aantal = int( input( 'Geef het aantal reizigers in: ' ) )
korting = 0

# Berekening van de kostprijzen:
totaal1 = aantal * 55
if aantal == 3:
    korting = 0.1
if aantal == 4:
    korting = 0.2
if aantal >= 5:
    korting = 0.4
totaal1 *= ( 1 - korting )

totaal2 = aantal * 49.95
if 4 <= aantal <= 5:
    totaal2 -= 49.95
if aantal >= 6:
    totaal2 -= 2 * 49.95

# Weergave van de mededeling
print("Verblijf 1 kost: €", round( totaal1, 2 ) )
print("Verblijf 2 kost: €", round( totaal2, 2 ) )

if totaal1 < totaal2:
    print("Verblijf 1 is goedkoper.")
else:
    print("Verblijf 2 is goedkoper.")
