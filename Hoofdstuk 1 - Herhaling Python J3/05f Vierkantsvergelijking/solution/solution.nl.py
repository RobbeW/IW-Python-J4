import math

# Coëfficienten vragen
a = float(input("Geef de waarde van a in: "))
b = float(input("Geef de waarde van b in: "))
c = float(input("Geef de waarde van c in: "))

# Berekening en printinstructies
print()
D = b**2 - 4*a*c
if D < 0 :
    print( 'Er zijn geen reële oplossingen.' )
elif D == 0:
    x = -b / ( 2 * a )
    print( 'Er is exact één reële oplossing, namelijk:', round( x, 2 ) )
else:
    x1 = round( ( -b + math.sqrt( D ) ) / ( 2 * a ), 2)
    x2 = round( ( -b - math.sqrt( D ) ) / ( 2 * a ), 2)
    
    
    
    print( 'Er zijn twee verschillende reële oplossingen, namelijk', min( x1, x2 ), 'en', max( x1, x2 ) )