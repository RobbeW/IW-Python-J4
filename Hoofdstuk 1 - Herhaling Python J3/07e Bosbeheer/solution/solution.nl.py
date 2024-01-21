import math

# Invoer
n = int(input("Geef het aantal bomen in: "))
perc = int(input("Geef het percentage in: "))
bijplanten = int(input("Geef het aantal nieuwe bomen in: "))

# Berekening
print("Er zijn eerst", n, "bomen in het bos.")
flag = True
i = 0
while flag:
    i += 1
    omhakken = math.floor( n*perc/100 )
    nieuw = n - omhakken + bijplanten
    flag = nieuw != n
    n = nieuw
    print("na", i, "jaar zijn er", n, "bomen.")

print("Er zullen uiteindelijk", n, "bomen in het bos zijn.")