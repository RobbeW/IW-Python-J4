# Gegevens vragen
n = int(input('Geef het getal in: '))

# Tekenen van de ASCII boom
for i in range(n + 2):
    aantal_kruisjes = 2 * i + 1
    aantal_spaties = n + 2 - i - 1
    print(aantal_spaties * " " + aantal_kruisjes * "X")

for i in range(2):
    print((n + 2 -1) * " " + "X")
