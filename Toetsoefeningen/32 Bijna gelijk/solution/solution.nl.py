def bijnagelijk( a, b, tolerantie ):
    return abs(a - b) < tolerantie

x = float(input( "Geef een eerste getal in: ") )
y = float(input( "Geef een eerste getal in: ") )
delta = float(input( "Geef een tolerantie in: ") )

print()
if bijnagelijk(x, y, delta):
    print( x, "en", y, "zijn bijna aan elkaar gelijk.")
else:
    print( x, "en", y, "verschillen teveel.")