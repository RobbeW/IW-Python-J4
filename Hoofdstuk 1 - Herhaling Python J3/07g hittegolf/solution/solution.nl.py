# Initialisatie
aantal_dagen = 0
aantal_dagen_30 = 0
hoogste = 0

# Lus
flag = True
while flag:
    temp = float( input( "Geef de maximale temperatuur in: " ) )
    aantal_dagen += 1
    if temp >= 30:
        aantal_dagen_30 += 1
    if temp > hoogste:
        hoogste = temp
    
    flag = aantal_dagen_30 < 3

# Eindweergave
print( "Er werden", aantal_dagen,"temperaturen ingevoerd." )
print( "De hoogste temperatuur was", hoogste,"°C." )