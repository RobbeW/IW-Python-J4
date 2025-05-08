import math

def kwadratisch_gemiddelde( lijst ):
    n = len(lijst)
    som = 0
    for getal in lijst:
        som += getal**2
    result = math.sqrt( 1 / n * som )
    return round( result, 3)
