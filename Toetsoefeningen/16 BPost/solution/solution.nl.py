# Invoer van massa en aantal
massa = float( input( 'Geef de massa in: ' ) )
aantal = float( input( 'Geef het aantal in: ' ) )

# Bepalen van de factor
if aantal >= 10:
    if massa >= 350:
        multi = 9.30
    elif massa >= 100:
        multi = 5.58
    else:
        multi = 3.72
else:
    if massa >= 350:
        multi = 9.45
    elif massa >= 100:
        multi = 5.67
    else:
        multi = 3.78

# Weergave
print()
print( 'U dient EUR', round( aantal * multi, 2), 'te betalen.' )
