# De 3 aparte cijfers opvragen
getal1 = int( input( 'Geef een getal van 3 cijfers in: ' ) )
getal2 = int( input( 'Geef een getal van 4 cijfers in: ' ) )
getal3 = int( input( 'Geef een getal van 3 cijfers in: ' ) )

# Bereking van het controlegetal
controle = (getal1 * 10000 * 1000 + getal2 * 1000 + getal3) % 97
if controle == 0:
    controle = 97

# Weergave van de mededeling
print("+++" + str(getal1).zfill(3) + "/" + str(getal2).zfill(4) + "/" + str(getal3).zfill(3) + str(controle).zfill(2) + "+++")