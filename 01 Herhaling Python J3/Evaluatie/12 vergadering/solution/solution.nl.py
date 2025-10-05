# Invoer vragen
uur1 = int( input( "Geef het startuur in: " ) )
min1 = int( input( "Geef de bijbehorende minuten in: " ) )

minuten = int( input( "Geef het aantal vergaderinminuten in: " ) )

pauzes = int( input( "Geef het aantal pauzes in: " ) )

# Berekeningen
min = ( min1 + minuten + pauzes * 20 ) % 60
uur = ( uur1 + ( min1 + minuten + pauzes * 20 ) // 60 ) % 24

# Uitvoer
print( "De vergadering eindigt om", str(uur)+"."+str(min), "u." )
