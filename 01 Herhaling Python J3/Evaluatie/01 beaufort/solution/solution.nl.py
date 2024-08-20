v = float( input( 'Geef de windsnelheid in km/u in:' ) )
v_fixed = v / 3.6

B = round( pow( v_fixed / 0.8360, 2/3 ), 0 )

print(int(B), 'Beaufort')