import math

# Invoer
n = int(input("Geef het aantal bomen in: "))
percentage = int(input("Geef het percentage in: "))
bijplanten = int(input("Geef het aantal nieuwe bomen in: "))

# Berekening
print("Er zijn eerst", n, "bomen in het bos.")
i = 0
while True:
    i += 1
    omhakken = math.floor( n*percentage/100 )
    nieuw = n - omhakken + bijplanten
    print("na", i, "jaar zijn er", nieuw, "bomen.")
    if nieuw == n:
        break
    else:
        n = nieuw

print("Er zullen uiteindelijk", n, "bomen in het bos zijn.")
