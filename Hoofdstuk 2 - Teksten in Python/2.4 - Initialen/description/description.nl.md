# 2.4 - Initialen

## De find-functie
Alle karakters in een lijst of een string hebben een **plaats of index,** net zoals een leerling een klasnummer kan hebben. Via dat getal kunnen we nagaan op welke plaats een karakter staat in een string of lijst. 

Voorbeeld: 
We hebben de string 'W8woord!' 

Wanneer we op zoek willen gaan naar de locatie van het uitroepteken, kunnen we gebruikmaken van volgende code: 
```
woord = 'W8woord!
index = woord.find('!')
print(index)
```
De uitkomst van deze code is: 

```
Uitvoer: 7
```
**Opgelet!**
Wanneer je de lengte van de string nagaat, bekom je echter: 
```
lengte = len(woord)
print(lengte)
```
De uitkomst van deze code is: 

```
Uitvoer: 8
```

Dit komt omdat de allereerste index het getal 0 krijgt. Wil je het eerste karakter uit een string bekomen, dan gaan we op zoek naar het karakter met indexnummer = 0. 
Wanneer we dat karakter met indexnummer 0 op het scherm willen printen, gebruiken we:

```
print(woord[0])
```


**Gegeven:**

Fred wil op de schermen van de laptops van de werknemers de initialen van het personeelslid laten verschijnen. Daarvoor wil hij een klein programma schrijven. 

<img src="https://images.pexels.com/photos/1229861/pexels-photo-1229861.jpeg" width="50%"/>

Daarvoor voert hij de volledige naam in van de gebruiker / het personeelslid. 
De computer moet dan op zoek gaan naar de eerste letter van de voornaam. 
Daarna naar de eerste letter van de familienaam. 

De eerste letter van de voornaam terugvinden is eenvoudig ... maar hoe bekom je de eerste letter van de achternaam? 

**Opgave:**
Ontwerp een algoritme dat: 

* Uit een ingevoerde naam (voornaam + achternaam) de eerste letter van de voornaam opzoekt; 
* Uit een ingevoerde naam (voornaam + achternaam) de eerste letter van de achternaam opzoekt; 
* Print te resultaten naar het scherm in een correcte volzin; 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 
* **Tip: een spatie is ook een karakter!** 