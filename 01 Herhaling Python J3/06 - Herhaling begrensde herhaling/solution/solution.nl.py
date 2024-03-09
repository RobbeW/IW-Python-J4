# Startgegevens
inwoners = 11697557
toename = 62770
jaar = 2023

eindjaar = int( input( "Geef het eindjaar in: " ) )
for i in range( jaar + 1, eindjaar + 1):
    inwoners += toename
    if i % 10 == 0:
        print( "In", i, "verwacht men", inwoners, "inwoners in België.")
