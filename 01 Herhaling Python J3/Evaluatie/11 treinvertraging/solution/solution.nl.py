# Invoer vragen
uur1 = int( input( "Geef het uur van vertrek in: " ) )
min1 = int( input( "Geef de minuten van vertrek in: " ) )

uur2 = int( input( "Geef het uur van de reistijd in: " ) )
min2 = int( input( "Geef de minuten van reistijd in: " ) )

vertraging = int( input( "Geef het aantal minuten vertraging in: " ) )

# Berekeningen
min = ( min1 + min2 + vertraging ) % 60
uur = ( uur1 + uur2 + (min1 + min2 + vertraging) // 60 ) % 24

# Uitvoer
print( "Je trein komt aan om", str(uur)+"."+str(min), "u." )
