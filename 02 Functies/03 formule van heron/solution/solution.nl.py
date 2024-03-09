import math

def oppervlakte( a, b, c ):
    s = 1 / 2 * ( a + b + c )
    A = math.sqrt( s * (s - a) * ( s - b ) * ( s - c ) )
    return round( A, 2 )