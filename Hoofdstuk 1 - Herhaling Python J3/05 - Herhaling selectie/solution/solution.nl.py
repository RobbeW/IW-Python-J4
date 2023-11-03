perc = float(input("Geef het percentage als kommagetal in:"))

if perc == 0:
    print("Toner is volledig leeg.")
    print("Je kan niet meer afdrukken.")
elif perc <= 0.10:
    print("Toner is bijna leeg.")
    print("Bestel een nieuwe toner.")
elif perc <= 0.25:
    print("Bestel een nieuwe toner.")
