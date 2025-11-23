aantalFlessen = int(input("Vul een aantal flesjes in: "))
aantalBakken = (aantalFlessen + 23) // 24 
aantalPaletten = (aantalBakken + 69) // 70 

if aantalBakken == 1:
    print("Voor", aantalFlessen, "flesjes voorziet de brouwer", aantalBakken, "bak en", aantalPaletten, "palet.")     
elif aantalPaletten == 1:
    print("Voor", aantalFlessen, "flesjes voorziet de brouwer", aantalBakken, "bakken en", aantalPaletten, "palet.")
else:
    print("Voor", aantalFlessen, "flesjes voorziet de brouwer", aantalBakken, "bakken en", aantalPaletten, "paletten.") 
