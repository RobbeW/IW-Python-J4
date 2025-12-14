aantalLiter = int(input("Hoeveel liter Cola werd vandaag geproduceerd: "))
aantalBlikjes = (aantalLiter * 100) // 33
aantalPakketten = (aantalBlikjes + 23) // 24 

if aantalPakketten == 1:
    print("Met", aantalLiter, "liter worden er", aantalBlikjes, "blikjes gevuld en", aantalPakketten, "pakket gemaakt.")
else:
    print("Met", aantalLiter, "liter worden er", aantalBlikjes, "blikjes gevuld en", aantalPakketten, "pakketten gemaakt.")
