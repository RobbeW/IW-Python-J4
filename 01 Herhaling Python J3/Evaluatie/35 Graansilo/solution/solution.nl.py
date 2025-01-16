# Invoer
massa = int(input("Geef het startmassa in (in kg): "))
verbruik = int(input("Geef het aantal kg dat dagelijks gebruikt wordt in: "))
oogst = int(input("Geef de eerste oogsthoeveelheid in: "))
toename = int(input("Geef de dagelijkse toename van deze oogsthoeveelheid in: "))

# Berekening
nieuw = massa - verbruik + oogst
i = 0
while nieuw < massa:
    print("Na dag", i + 1, "bevat de silo", nieuw ,"kg graan.")
    i+=1
    massa = nieuw
    oogst += toename
    nieuw = massa - verbruik + oogst
    
# Uiteindelijk
if i == 1:
    print("De silo bevatte het minste graan na één dag, namelijk", massa, "kg.")
else:
    print("De silo bevatte het minste graan na", i, "dagen, namelijk", massa, "kg.")
