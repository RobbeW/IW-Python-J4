# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
som = 0
for i in range( 1, n):
    if n % i == 0:
        som += i
print()
# Weergave
if som == n:
    print(n, "is een perfect getal.")
else:
    print(n, "is geen perfect getal.")
