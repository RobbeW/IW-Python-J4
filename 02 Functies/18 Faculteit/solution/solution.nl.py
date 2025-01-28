def faculteit(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

# Invoer vragen
n = int(input("Geef het rangnummer in: "))
opl = faculteit(n)

print(str(n)+"! is gelijk aan", opl)
