g1 = int( input( 'Geef het aantal uur in van video 1: '))
d1 = int( input( 'Geef het aantal minuten in van video 1: '))
e1 = int( input( 'Geef het aantal seconden in van video 1: '))

g2 = int( input( 'Geef het aantal uur in van video 2: '))
d2 = int( input( 'Geef het aantal minuten in van video 2: '))
e2 = int( input( 'Geef het aantal seconden in van video 2: '))

e = (e1+e2) % 12
d = (d1 + d2 + (e1+e2)//12)%12
g = g1+g2 + (d1 + d2 + (e1+e2)//12) // 12

print('Totale aantal eieren:', g, 'gross,', d, 'dozijn en', e, 'eieren.')