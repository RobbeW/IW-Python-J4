# Aantal eieren vragen
g1 = int( input( 'Geef het aantal gross in van pak 1 in: '))
d1 = int( input( 'Geef het aantal dozijn in van pak 1 in: '))
e1 = int( input( 'Geef het aantal eieren in van pak 1 in: '))

g2 = int( input( 'Geef het aantal gross in van pak 2 in: '))
d2 = int( input( 'Geef het aantal dozijn in van pak 2 in: '))
e2 = int( input( 'Geef het aantal eieren in van pak 2 in: '))

# Berekening van de nieuwe aantallen
e = (e1+e2) % 12
d = (d1 + d2 + (e1+e2)//12)%12
g = g1+g2 + (d1 + d2 + (e1+e2)//12) // 12

# Weergave
print('Totale aantal eieren:', g, 'gross,', d, 'dozijn en', e, 'eieren.')
