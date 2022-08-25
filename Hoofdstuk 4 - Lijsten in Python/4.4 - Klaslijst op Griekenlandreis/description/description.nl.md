# Klaslijst op Griekenlandreis
**Gegeven:** 

Bij de vorige oefening hebben we via **lijsten, de appendfunctie en andere functies** de nieuwe eerstejaars verdeeld over de klassen. Dat kan eigenlijk een heel stuk efficiënter! 

Op Griekenlandreis hebben we een grote(re) groep leerlingen mee. Die moeten op de boot verdeeld worden over de verschillende kabines. 


We krijgen volgende lijsten: 
```
namen = ['Malina', 'Briek', 'Rémi', 'Ferit', 'Agon', 'Thomas', 'Julie', 'Floor', 'Menke', 'Bastiaan', 'Camu', 'Mateo', 'Mathias', 'Amélie', 'Julien', 'Veronika', 'Alice', 'Sieben', 'Marit', 'Hanne', 'Pieter-Jan', 'Jules', 'Oscar', 'Sanne', 'Tarik', 'Berfin', 'Lotte', 'Sien', 'Caro', 'Louise', 'Theo', 'Julie']
kamer = [201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226]
```

Je krijgt van de reisleider de opdracht om de leerlingen te verdelen over de verschillende kamers. Zo kunnen we een overzichtelijke lijst afgeven aan de receptie en andere begeleiders. 

```
201 = []
202 = []
209 = []
218 = []
220 = []
221 = []
224 = []
226 = []
```

<img src="https://images.pexels.com/photos/1518498/pexels-photo-1518498.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" width="50%"/>

## **Itereren over een lijst**
Het **programmeerconcept 'De Begrensde Herhaling** ken je reeds. Je kan deze gebruiken om exact aantal keer te herhalen. Dit deden we via volgende syntax:

```
for teller in range (begingetal, eindgetal): 
# teller zal bij deze telkens +1 gaan.
# begingetal zit binnen deze herhaling, eindgetal niet! 
```

Je kan bovenstaande functie ook gebruiken om **te itereren over lijsten!**. 
```
for teller_1, teller_2 in zip (namen, kamer): 
# We gebruiken hier twee tellers. 
# Zo selecteren we item_1 uit de lijst namen en item_1 uit de lijst kamer. 
```
Je krijgt reeds volgende code: 
```
# Gegeven:
namen = ['Malina', 'Briek', 'Rémi', 'Ferit', 'Agon', 'Thomas', 'Julie', 'Floor', 'Menke', 'Bastiaan', 'Camu', 'Mateo', 'Mathias', 'Amélie', 'Julien', 'Veronika', 'Alice', 'Sieben', 'Marit', 'Hanne', 'Pieter-Jan', 'Jules', 'Oscar', 'Sanne', 'Tarik', 'Berfin', 'Lotte', 'Sien', 'Caro', 'Louise', 'Theo', 'Julie']
kamer = [201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226, 201, 202, 209, 218, 220, 221, 224, 226]
kamer_201 = []
kamer_202 = []
kamer_209 = []
kamer_218 = []
kamer_220 = []
kamer_221 = []
kamer_224 = []
kamer_226 = []

# HIER ONTBREEKT EEN VOORWAARDE!

    if teller_2 == 201: 
        kamer_201.append(teller_1)
    elif teller_2 == 202: 
        kamer_202.append(teller_1)
    elif teller_2 == 209: 
        kamer_209.append(teller_1)
    elif teller_2 == 218: 
        kamer_218.append(teller_1)
    elif teller_2 == 220: 
        kamer_220.append(teller_1)
    elif teller_2 == 221: 
        kamer_221.append(teller_1)
    elif teller_2 == 224: 
        kamer_224.append(teller_1)
    elif teller_2 == 226: 
        kamer_226.append(teller_1)

# Output
print("In de kajuit 201 zitten volgende leerlingen: ", kamer_201)
# HIER ONTBREKEN NOG OUTPUTS
```

**Opgave:**
Bekijk bovenstaande algoritme. 
Vul de ontbrekende coderegels zoals de voorwaarde en de output verder aan. 

* Gebruik voor jouw algoritme een begrensde herhaling om te **itereren over een lijst**; 
* Laat de resultaten verschijnen met een verzorgde volzin; 
* Een volzin bevat een onderwerp, werkwoordsvorm, hoofdletters, leestekens ... 
* Bijvoorbeeld: "In de kajuit 201 zitten volgende leerlingen: ... "
