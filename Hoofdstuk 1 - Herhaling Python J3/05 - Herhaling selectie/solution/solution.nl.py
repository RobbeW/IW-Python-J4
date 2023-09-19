# Invoer
niveau = float( input('Geef het tonerniveau (in percentage): '))

# Verwerking en afdrukken
print()
if niveau == 0:
    print("Toner is volledig leeg.")
    print("Je kan niet meer afdrukken.")
elif niveau <= 0.10:
    print("Toner is bijna leeg.")
    print("Bestel een nieuwe toner.")
elif niveau <= 0.25:
    print("Bestel een nieuwe toner.")