getal = int( input( "Geef een getal in: " ) )
is_priem = True
for i in range(2, getal):
    if getal % i == 0:
        is_priem = False

if is_priem:
    print(getal, "is priem.")
else:
    print(getal, "is niet priem.")
