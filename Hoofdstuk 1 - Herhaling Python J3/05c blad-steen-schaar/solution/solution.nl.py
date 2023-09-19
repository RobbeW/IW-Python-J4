# Invoer
woord1 = input( "Geef het woord van speler 1 in: ")
woord2 = input( "Geef het woord van speler 2 in: ")

# Verwerking en uitvoer
if woord1 == woord2:
    print( 'onbeslist' )
elif woord1 == 'paper' and woord2 == 'rock':
    print( 'speler 1 wint' )
elif woord1 == 'rock' and woord2 == 'scissors':
    print( 'speler 1 wint' )
elif woord1 == 'scissors' and woord2 == 'paper':
    print( 'speler 1 wint' )
else: 
    print( 'speler 2 wint' )