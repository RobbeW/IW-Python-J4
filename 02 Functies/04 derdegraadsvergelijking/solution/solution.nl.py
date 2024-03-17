def discriminant( p, q ):
    D = -4 * p ** 3 -27 * q ** 2
    if D > 0 :
        print( 'Er zijn drie verschillende reële oplossingen.' )
    elif D < 0:
        print( 'Er is exact één reële oplossing.' )
    else:
        print( 'Van de drie oplossingen zijn er minstens twee aan elkaar gelijk.' )
    
    return D

# Invoer vragen
p = int(input())
q = int(input())

# Uitvoer
discriminant( p, q )
