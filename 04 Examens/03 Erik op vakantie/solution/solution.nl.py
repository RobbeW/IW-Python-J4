def kostAuto(km): 
   prijs = km * 0.15 
   return prijs 

def kostVliegen(kmVliegen, kmInStad): 
   vliegPrijs = 30 * kmVliegen * 3 / 1000 
   autoHuur = 100 
   totaalPrijs = vliegPrijs + autoHuur + kostAuto(kmInStad) 
   return totaalPrijs 

kmNaarBestemming = int(input("Hoeveel km is het tot de vakantiebestemming?")) 
kmOpBestemming = int(input("Hoeveel km wil je rijden op de vakantiebestemming?")) 

kostEnkelAuto = kostAuto(kmNaarBestemming * 2 + kmOpBestemming) 
kostVliegtuig = kostVliegen(kmNaarBestemming * 2, kmOpBestemming) 

if kostEnkelAuto < kostVliegtuig: 
   print("Je gaat beter met de auto, je bespaart dan €", kostVliegtuig - kostEnkelAuto) 
else: 
   print("Je gaat beter met het vliegtuig, je bespaart dan €", kostEnkelAuto - kostVliegtuig) 