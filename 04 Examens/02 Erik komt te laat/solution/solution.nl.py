aantalKeerTeLaat = int(input("Hoe vaak kwam je al te laat?"))

if aantalKeerTeLaat <= 2:
    print("Er zijn geen gevolgen.")
elif aantalKeerTeLaat <= 3:
    print("Kijk uit! Het is je derde maal te laat. Een volgende keer zal gesanctioneerd worden.")
elif aantalKeerTeLaat <= 4:
    print("Jammer maar helaas… Dat zal aanstaande vrijdag strafstudie worden. Volgende keer beter!")
else:
    print("Oei, dit wordt wel echt problematisch he. Dit is al je", str(aantalKeerTeLaat) + "e keer te laat. Het is jammer, maar dat is strafstudie VANAVOND.")