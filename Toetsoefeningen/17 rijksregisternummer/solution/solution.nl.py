# Vraag naar de zijden
jaar = int( input( "Geef het geboortejaar: " ) )
maand = int( input( "Geef de geboortemaand: " ) )
dag = int( input( "Geef de geboortedag: " ) )
dagteller = int( input( "Geef de dagteller: " ) )

# Controlegetal bepalen
som = (jaar % 100) * 10**7 + maand * 10**5 + dag * 10**3 + dagteller
if jaar >= 2000:
    som += 2* 10**9

cg = 97 - som % 97

# Weergave op het scherm
print()
print( "Het rijksregisternummer is "+str(jaar%100).zfill(2)+"."+str(maand).zfill(2)+"."+str(dag).zfill(2)+"-"+str(dagteller).zfill(3)+"-"+str(cg).zfill(2)+"." )
