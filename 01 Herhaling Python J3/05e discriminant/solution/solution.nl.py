# Coëfficienten vragen
a = float(input("Geef de waarde van a in: "))
b = float(input("Geef de waarde van b in: "))
c = float(input("Geef de waarde van c in: "))

# Berekening en printinstructies
D = round( b**2 - 4 * a * c, 1 )
print( 'Discriminant =', D )
if D > 0:
    print( 'Er zijn twee verschillende reële oplossingen.')
elif D < 0:
    print( 'Er zijn geen reële oplossingen.')
else:
    print( 'Er is exact één reële oplossing.')
