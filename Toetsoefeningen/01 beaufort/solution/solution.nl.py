v = float( input( 'Geef de windsnelheid in m/s in:' ) )

B = round( pow( v / 0.8360, 2/3 ), 0 )

print(int(B), 'Beaufort')