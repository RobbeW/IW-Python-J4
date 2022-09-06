# 2.5 - Karakter Vervangen

## De Replace-functie

Binnen Python is het mogelijk om, in een beweging, een karakter te vinden en deze te vervangen voor een andere karakter. Dit kan je gebruiken om bijvoorbeeld een onbedoelde spatie of speciaal teken aan te passen. 

De **syntax** van de **replace()-functie** gaat als volgt: 
```
email = 'fred.deboosere€holdthedoor.be'
email = email.replace('€', '@')
print(email)

```
Dus de functie werkt met **twee parameters**, namelijk replace(oude karakter, nieuwe karakter). 

**Gegeven:**

Door een corrupte database komen heel wat e-mailadressen het klantenbestand binnen in een verkeerd format. Sommige bevatten nodeloze spaties, of hebben een speciaal teken in de plaats van een @-teken.

<img src="https://images.pexels.com/photos/1591062/pexels-photo-1591062.jpeg" width="50%"/>

**Opgave:**
Fred krijgt volgende e-mailadressen: 

```
voyewa6988!telenet.be
hansen70€gmail.com
atla3tiovity?proximus.be
```

Ontwerp een algoritme dat: 
* De foute karakters uit de ingevoerde e-mailadressen kan halen en vervangen door een @-teken;
* Uitbreiding: maak gebruik van een lijst. 
* Print de correcte e-mailadressen naar het scherm; 
* **Test** en **debug** voor je indient. 