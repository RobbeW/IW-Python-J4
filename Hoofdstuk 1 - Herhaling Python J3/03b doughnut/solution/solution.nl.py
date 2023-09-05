PI = 3.141592

r = float( input( 'Geef de kleine straal in:' ) )
R = float( input( 'Geef de grote straal in:' ) )

A = 4 * pow( PI, 2 ) * r * R
V = 2 * pow( PI, 2 ) * pow( r, 2 ) * R

print('\nOppervlakte: {} cm²'.format( round( A, 3 ) ) )
print('Volume: {} cm³'.format( round( V, 3 ) ) )