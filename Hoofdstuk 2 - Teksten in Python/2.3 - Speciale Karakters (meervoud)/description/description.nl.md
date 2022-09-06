# 2.3 - Speciale Karakters



<img src="https://media.istockphoto.com/videos/login-web-page-closeup-video-id1202008385?b=1&k=20&m=1202008385&s=640x640&h=-4Sf9O5Bv_1eyKcFky-_SwbrE6UERejS5P0sBwFU0-w=" width="50%"/>

**Gegeven:** 

Fred wil binnen zijn bedrijf een eenvoudige tool ontwerpen om te controleren of een wachtwoord voldoende sterk is. 
Daarvoor deelt hij het probleem op in kleine tussenstappen. Zo zal hij nu controleren of het wachtwoord een **speciale karakters** bevat. 
Dus meer dan enkel het !-teken uit de vorige opgave. 

Hij wil op zoek gaan naar volgende tekens: 

```
speciale_karakters = ['!', '?', '&', '#', 'ç']
```


Indien het wachtwoord onvoldoende sterk is, dus geen van die tekens bevat, verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Uw wachtwoord bevat geen speciaal teken.  
```

Indien het wachtwoord voldoende sterk is, en dus **minstens één van die tekens bevat,** verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Goed zo! Uw wachtwoord bevat minstens één speciaal teken!
```

Voor deze oefening kan je gebruikmaken van de: 
* count()-functie
* lijsten (uitbreiding)

**Startcode:**
```
speciale_karakters = ['!', '?', '&', '#', 'ç']
teller = 0
wachtwoord = input('Wat is het wachtwoord?')
```


**Opgave:**
Ontwerp een algoritme dat: 

* Vraagt naar een mogelijk wachtwoord; 
* Het aantal speciale tekens nagaat; 
* In een volzin kan weergeven of het gekozen wachtwoord voldoet aan de voorwaarden (minimaal 8 tekens); 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 