# Vraag naar 3 getallen
a = int(input("Geef het eerste getal in: "))
b = int(input("Geef het tweede getal in: "))
c = int(input("Geef het derde getal in: "))

# Gesorteerd
mi = min(a, b, c)
ma = max(a, b, c)
me = a + b + c - mi - ma

# Keuze
if me - mi == ma - me:
    print(2 * ma - me)
elif me - mi < ma - me:
    print(2 * me - mi)
else:
    print(mi + ma - me)
