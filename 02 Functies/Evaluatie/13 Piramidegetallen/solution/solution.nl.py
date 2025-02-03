def piramidegetal(n):
    som = 0
    for i in range(n):
        som += (i + 1)**2
    return som

n = int(input("Geef het rangnummer in: "))

antwoord = piramidegetal(n)

if n == 1:
    print("Het allereerste piramide getal is", antwoord)
else:
    print("Het", n, "e piramidegetal is", antwoord)
