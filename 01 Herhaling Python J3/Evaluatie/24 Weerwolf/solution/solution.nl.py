# Invoer
wachtrij = int(input("Geef het aantal mensen in: "))
toename = int(input("Geef het aantal mensen dat er bijkomt in: "))
afname = int(input("Met welk aantal neemt dit af?: "))

# Berekening
voorwaarde = True
i = 0
while voorwaarde:
    i+=1
    berekening = wachtrij - 24 + toename
    toename = toename - afname
    
    if berekening <= wachtrij:
        voorwaarde = False
    else:
        wachtrij = berekening
        print("Na", i*3, "minuten bevat de wachtrij", wachtrij, "personen")

# Uiteindelijk
print("De wachtrij was het langst na", (i-1)*3, "minuten.")
