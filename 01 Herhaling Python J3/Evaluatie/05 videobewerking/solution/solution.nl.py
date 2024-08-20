# Tijdsgegevens vragen
h1 = int( input( 'Geef het aantal uur in van video 1: '))
m1 = int( input( 'Geef het aantal minuten in van video 1: '))
s1 = int( input( 'Geef het aantal seconden in van video 1: '))

h2 = int( input( 'Geef het aantal uur in van video 2: '))
m2 = int( input( 'Geef het aantal minuten in van video 2: '))
s2 = int( input( 'Geef het aantal seconden in van video 2: '))

# Nieuwe tijd berekenen
s = (s1+s2) % 60
m = ( (m1+m2)  + (s1+s2) // 60 ) % 60
h = (h1+h2) + ( (m1+m2)  + (s1+s2) // 60 )//60

# Weergave
print('Totale tijd:', h, 'uur,', m, 'minuten en', s, 'seconden.')
