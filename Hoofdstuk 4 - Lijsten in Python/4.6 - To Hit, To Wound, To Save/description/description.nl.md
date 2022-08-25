**Gegeven:**

Tijdens de spelletjesavond op woensdag besluit de groep een ander spelletje uit de kast te halen. Ze kiezen ervoor om een spelletje Warhammer te spelen. 
Daar nemen twee legers het tegen elkaar op en worden veel, heel veel, dobbelstenen gerold. Alle dobbelstenen zijn D6. 

<img src="https://cdnb.artstation.com/p/assets/images/images/030/189/101/large/dmitriy-mironov-detals-06.jpg?1599854678" width="50%"/>

De soldaten van het ene leger voeren een aanval uit op de troepen van het andere leger. 
De tien soldaten voeren elk 4 aanvallen uit met hun speren, dus maar liefst 40. Maar een aanval uitvoeren is nog maar het begin. 
Een aanval moet: 
* raken; 
* verwonden; 
* voorbij het harnas van de vijand raken. 

De soldaten zijn vrij krachtig en hebben volgende eigenschappen met hun wapens: 
* Stap 1: op 2+ raken ze hun doel; 
* Stap 2: op een 3+ verwonden ze de tegenstrever; 
* Stap 3: op een 6 raakt de speer het harnas en wordt géén verwonding toegebracht. 


**Opgave:**
Ontwerp een algoritme dat kan berekenen hoeveel verwondingen werden toegebracht. Je krijgt volgende codes om je te helpen: 

```
import random 
resultaten = []

# Raken van het doel: 
for i in range (0, 40): 
    dobbelsteen = random.randint(1,6)
    resultaten.append(dobbelsteen)
aantal_succes = resultaten.count(2) + resultaten.count(3) + resultaten.count(4) + resultaten.count(5) + resultaten.count(6)
resultaten = []

# Verwonden van het doel: 
for i in range (0, ... ): 

# Hoeveel verwondingen worden gered door het harnas: 

```

* Gebruik je kennis en vaardigheden in Python-code om een algoritme te ontwerpen; 
* Maak voor jouw algoritme gebruik van volgende functies: **random, lijsten, begrensde herhaling**; 
* Print te resultaten naar het scherm in een correcte volzin; 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 
