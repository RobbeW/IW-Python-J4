import math

# Invoer
n = int(input("Geef het aantal bomen in: "))
perc = int(input("Geef het percentage in: "))
bijplanten = int(input("Geef het aantal nieuwe bomen in: "))

# Berekening
print()
print("Er zijn eerst", n, "bomen in het bos.")
for i in range(100):
    omhakken = math.floor( n*perc/100 )
    n = n - omhakken + bijplanten
    if (i+1) % 10 == 0:
        print("na", i+1, "jaar zijn er", n, "bomen.")
