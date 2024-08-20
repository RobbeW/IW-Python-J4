# Invoer
l = int(input("Geef het aantal hoorns links in: "))
r = int(input("Geef het aantal hoorns rechts in: "))

# Uitvoer
if l == r == 0:
    print("Geen eland")
elif l == r:
    print(f"{2*l} even")
else:
    print(f"{2*max(l,r)} oneven")
