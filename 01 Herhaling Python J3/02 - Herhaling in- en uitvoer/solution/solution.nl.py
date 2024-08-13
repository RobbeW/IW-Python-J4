# Invoer van variabelen
voornaam = input("Geef de eerste voornaam in: ")
leeftijd = int(input("Geef je leeftijd in: "))

te_doen = 100 - leeftijd
te_doen *= 365.25

# Uitvoer
print(voornaam + ", het duurt nog ongeveer", round(te_doen), "dagen tot je 100 jaar bent!")
