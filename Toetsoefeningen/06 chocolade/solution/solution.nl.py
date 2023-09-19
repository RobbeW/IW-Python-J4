massa = int( input( 'Geef de gewenste massa: ') )

aantal600 = massa // 600
rest600 = massa % 600
aantal120 =  rest600 // 120
rest120 = rest600 % 120
aantal40 = rest120 // 40

print( 'aantal repen van 600 g:', aantal600 )
print( 'aantal repen van 120 g:', aantal120 )
print( 'aantal repen van 40 g:', aantal40 )