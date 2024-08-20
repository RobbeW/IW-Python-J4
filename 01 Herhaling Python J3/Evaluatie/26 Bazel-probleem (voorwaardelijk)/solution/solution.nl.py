import math

# Invoer
n = int(input("Geef het aantal termen op: "))

# Berekening
som = 0
i = 0
while i < n:
    som += 1/(i+1)**2
    i += 1

benadering = math.sqrt(6 * som)

# Weergave
print( "De Bazel-benadering van pi met", n, "termen is", round(benadering, 6 ) )
