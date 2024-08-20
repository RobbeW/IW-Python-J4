# Initialisatie
aantal_dagen = 0
aantal_dagen_30 = 0
hoogste = 0

# Lus
while True:
    temp = float( input( "Geef de maximale temperatuur in: " ) )
    aantal_dagen += 1
    if temp >= 30:
        aantal_dagen_30 += 1
    if temp > hoogste:
        hoogste = temp
    
    if aantal_dagen_30 == 3:
        break

# Eindweergave
print( "Er werden", aantal_dagen,"temperaturen ingevoerd." )
print( "De hoogste temperatuur was", hoogste,"°C." )
