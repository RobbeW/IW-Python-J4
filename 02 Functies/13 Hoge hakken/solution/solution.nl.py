def wankelfactor(aantal_uur):
    result = 28 / (45 * (0.5 * aantal_uur + 1))
    return round(result, 2)

def hakhoogte(s, w = 0.5):
    result = w * (12 + 0.375 * s)
    return round(result, 1)

# Invoer vragen
s = float(input("Geef de schoenmaat (Brits) in: "))
lang = input("Zal je de hakken lang dragen? Moet ik daar rekening mee houden? (J/N) ")

if lang != "J":
    h = hakhoogte(s)
else:
    A = float(input("Geef het aantal uur in: "))
    w = wankelfactor(A)
    h = hakhoogte(s, w)

print(f"Je mag hakken tot {h} cm dragen.")
