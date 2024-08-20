# Invoer vragen
v = float( input( 'Geef de windsnelheid in km/u in: ' ) )

# Omzetten naar m/s
v_fixed = v / 3.6

# Uitrekenen van Beaufort schaal
B = round( pow( v_fixed / 0.8360, 2/3 ), 0 )

# Weergave
print(int(B), 'Beaufort')
