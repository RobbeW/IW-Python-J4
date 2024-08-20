# Vraag het aantal sterren
n = int(input("Geef het aantal sterren in: "))

# Uitvoer verzorgen
for i in range(2, n):
    if (n - i) % (2*i-1) == 0 or n % (2*i-1) == 0 or 2*i -1 == n:
        print(f"{i} ; {i-1}")
    if n % i == 0:
        print(f"{i} ; {i}")
