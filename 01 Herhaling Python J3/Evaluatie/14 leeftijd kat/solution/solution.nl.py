# Vraag naar het aantal jaar
katjaar = int( input( 'Geef het aantal katjaren in: ' ) )

# Bepalen van het aantal katjaren
if katjaar == 1:
    mensjaar = 15
elif katjaar == 2:
    mensjaar = 15 + 9
else:
    mensjaar = 15 + 9 + ( katjaar - 2 ) * 4

# Weergeven van het aantal mensjaren
print( 'Een kat van', katjaar, 'jaar is', mensjaar, 'jaar in mensenjaren!' )
