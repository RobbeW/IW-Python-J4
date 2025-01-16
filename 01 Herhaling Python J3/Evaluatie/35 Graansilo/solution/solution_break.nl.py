# Invoer
massa = int(input("Geef het startmassa in (in kg): "))
verbruik = int(input("Geef het aantal kg dat dagelijks gebruikt wordt in: "))
oogst = int(input("Geef de eerste oogsthoeveelheid in: "))
toename = int(input("Geef de dagelijkse toename van deze oogsthoeveelheid in: "))

# Berekening
i = 0
while True:
    nieuw = massa - verbruik + oogst
    if nieuw >= massa:
        break
    i+=1
    print("Na dag", i, "bevat de silo", nieuw ,"kg graan.")
    massa = nieuw
    oogst += toename

# Uiteindelijk
if i == 1:
    print("De silo bevatte het minste graan na één dag, namelijk", massa, "kg.")
else:
    print("De silo bevatte het minste graan na", i, "dagen, namelijk", massa, "kg.")
