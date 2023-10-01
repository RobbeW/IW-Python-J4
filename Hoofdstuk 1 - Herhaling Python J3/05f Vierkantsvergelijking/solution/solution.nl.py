import math

# Coëfficienten vragen
a = float(input("Geef de waarde van a in: "))
b = float(input("Geef de waarde van b in: "))
c = float(input("Geef de waarde van c in: "))

# Berekening en printinstructies
D = b**2 - 4*a*c
if D < 0 :
    print( 'Er zijn geen reële oplossingen.' )
elif D == 0:
    x = -b / ( 2 * a )
    print( 'Er is exact één reële oplossing, namelijk:', round( x, 2 ) )
else:
    x1 = ( -b + math.sqrt( D ) ) / ( 2 * a )
    x2 = ( -b - math.sqrt( D ) ) / ( 2 * a )
    print( 'Er zijn twee verschillende reële oplossingen, namelijk', round( x1, 2 ), 'en', round( x2, 2 ) )