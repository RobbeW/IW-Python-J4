# 2.2 - Speciaal Karakter
## De count()-functie in Python

Wanneer je een sterk wachtwoord wil maken, moet dat wachtwoord aan een aantal eisen voldoen. Zoals: 
* lengte van het wachtwoord bedraagt acht tekens of meer; 
* **het wachtwoord bevat een speciaal teken;**
* het wachtwoord bevat een hoofdletter en een kleine letter.

Wanneer je wil nagaan dat een string een bepaald karakter bevat, kunnen we gebruikmaken van de count-functie. 
Deze kan tellen (=to count) hoeveel keer een bepaald karakter voorkomt in een string. 

```
string = "W8woord!"
print(string.count('!'))
```

De count()-functie kent volgende **syntax:**
```
naam_variabale_met_datatype_string.count("X")
X is wat je wilt tellen in de string. 
```


<img src="https://media.istockphoto.com/videos/login-web-page-closeup-video-id1202008385?b=1&k=20&m=1202008385&s=640x640&h=-4Sf9O5Bv_1eyKcFky-_SwbrE6UERejS5P0sBwFU0-w=" width="50%"/>

**Gegeven:** 
Fred wil binnen zijn bedrijf een eenvoudige tool ontwerpen om te controleren of een wachtwoord voldoende sterk is. 
Daarvoor deelt hij het probleem op in kleine tussenstappen. Zo zal hij nu controleren of het wachtwoord een speciaal karakter bevat. 
Hij wil nagaan of het wachtwoord het !-teken gebruikt. 

Indien het wachtwoord onvoldoende sterk is, verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Uw wachtwoord bevat geen speciaal teken.  
```

Indien het wachtwoord voldoende sterk is, verschijnt een gepaste boodschap op het scherm, namelijk: 
```
Goed zo! Uw wachtwoord bevat een speciaal teken!
```



**Opgave:**
Ontwerp een algoritme dat: 

* Vraagt naar een mogelijk wachtwoord; 
* Het aantal !-tekens telt; 
* In een volzin kan weergeven of het gekozen wachtwoord voldoet aan de voorwaarden (minimaal 8 tekens); 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 