# Invoer van variabelen
voornaam = input("Geef je voornaam in: ")
naam = input("Geef je naam in: ")
nettoloon_per_maand = float(input("Geef je netto maandloon in: "))
leeftijd = input("Geef je leeftijd in: ")

# Berekening
jaarloon = round( 13 * nettoloon_per_maand, 2 )

# Uitvoer
print(voornaam, naam, "van", leeftijd, "krijgt een jaarloon van €", jaarloon)
