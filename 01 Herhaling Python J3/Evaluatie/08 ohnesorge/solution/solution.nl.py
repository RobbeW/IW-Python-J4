import math

# Invoer vragen
vloeistof = input( 'Geef de naam van de vloeistof: ')
neta = float(input( 'Geef de viscositeit in (in kg/(m s)): ') )
rho = float(input( 'Geef de massadichtheid in (in kg/m³): '))
d = float(input( 'Geef de diameter in (in μm): '))
sigma = float(input( 'Geef de oppervlaktespanning in (in N/m): '))

# Berekening
ohne = round( neta / math.sqrt( rho * d * 10**-6 * sigma), 3)

# Uitvoer
print("Het Ohnsorge getal van kleine druppels", vloeistof, "is", str( ohne )+".")
