inwoners = 11697557
toename = 62770
jaar = 2023

eindjaar = int( input( "Geef het eindjaar in: " ) )
for i in range( jaar, eindjaar):
    jaar += 1
    inwoners += toename
    if jaar % 10 == 0:
        print( "In", jaar, "verwacht men", inwoners, "inwoners in België.")
       
if jaar % 10 != 0: 
    print( "In", eindjaar, "verwacht men", inwoners, "inwoners in België.")
