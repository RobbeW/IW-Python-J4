# Invoer
wachtrij = int(input("Geef het aantal mensen in: "))
toename = int(input("Geef het aantal mensen dat er bijkomt in: "))
afname = int(input("Met welk aantal neemt dit af?: "))

# Berekening
i = 0
vorige = wachtrij - 1
while vorige < wachtrij:
    vorige = wachtrij
    
    i+=1
    wachtrij = wachtrij - 24 + toename
    toename = toename - afname
    if wachtrij > vorige:
        print("Na", i*3, "minuten bevat de wachtrij", wachtrij, "personen")

# Uiteindelijk
print("De wachtrij was het langst na", (i-1)*3, "minuten.")
