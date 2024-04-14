# Invoer
getal = int(input("Geef het getal in: "))
bron = getal

# Berekening
i = 1
som = 0
while getal // 1 != 0:
    E = getal % 10
    som += i*E
    i+=1
    getal //= 10

# Weergave
laatste = str(bron % 100).zfill(2)
voorlaatste = str(bron // 100)

print("Het CAS-nummer is:",voorlaatste + "-"+laatste+"-"+str(som%10))
