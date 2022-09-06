# 2.1 - Lengte Wachtwoord
## De len()-functie in Python

Wanneer je een sterk wachtwoord wil maken, moet dat wachtwoord aan een aantal eisen voldoen. Zoals: 
* lengte van het wachtwoord bedraagt acht tekens of meer; 
* het wachtwoord bevat een speciaal teken;
* het wachtwoord bevat een hoofdletter en een kleine letter.

Wanneer we de **lengte van een string** willen nagaan, dan tellen we eigenlijk het aantal karakters in die string. 
Daarvoor maken we gebruik van een Python-functie. 

```
string = "W8woord!"
print(len(string))
```

De len()-functie kent volgende **syntax:**


<img src="https://media.istockphoto.com/videos/login-web-page-closeup-video-id1202008385?b=1&k=20&m=1202008385&s=640x640&h=-4Sf9O5Bv_1eyKcFky-_SwbrE6UERejS5P0sBwFU0-w=" width="50%"/>

**Gegeven:** 
Fred wil binnen zijn bedrijf een eenvoudige tool ontwerpen om te controleren of een wachtwoord voldoende sterk is. 
Daarvoor deelt hij het probleem op in kleine tussenstappen. Zo zal hij eerst controleren of het wachtwoord voldoende 
**lang** is. Met andere woorden: bevat het wachtwoord minstens het gevraagde aantal karakters. 

Indien het wachtwoord onvoldoende lang is, verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Uw wachtwoord bevat slecht X tekens. Het minimum aantal tekens is Y. 
```

Indien het wachtwoord voldoende lang is, verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Goed zo! Uw wachtwoord bevat Y tekens. 
```



**Opgave:**
Ontwerp een algoritme dat: 

* Vraagt naar een mogelijk wachtwoord; 
* Het aantal karakters berekent; 
* In een volzin kan weergeven of het gekozen wachtwoord voldoet aan de voorwaarden (minimaal 8 tekens); 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 