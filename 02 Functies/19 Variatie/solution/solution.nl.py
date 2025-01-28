def faculteit(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def variatie(n, k):
    teller = faculteit(n)
    noemer = faculteit(n-k)
    
    return teller // noemer

# Invoer vragen
n = int(input("Geef het aantal opties in: "))
k = int(input("Geef het aantal keuzes in: "))

opl = variatie(n, k)

print("Er zijn", opl, "mogelijkheden voor",k ,"verschillende keuzes uit", n, "opties.")
