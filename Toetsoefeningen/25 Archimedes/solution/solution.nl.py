# Invoer
n = int(input("Geef het aantal termen op: "))

# Berekening
som = 0
for i in range(n):
    som += 1/4**(i+1)

# Weergave
print( "Bij", n, "termen is de som van de Archimedes reeks", round(som, 9 ) )
