**Lijsten in Python**

Binnen Python kennen verschillende datatypes. We leerden reeds over:
* **strings:** een reeks aan karakters zoals een naam, adres, plaatsnaam ... strings worden gekenmerkt door de **aanhalingstekens**
* **integers:** gehele getallen waarmee we kunnen rekenen, zoals 1, 4, 512, 42, 404, 420 ... 
* **floats:** decimale getallen waarmeee we kunnen rekenen, zoals 3.14, 5.45 ... 

**Lijsten** worden gekenmerkt door de vierkante haakjes [] waartussen we **items** kunnen bewaren. 
Die **items** kunnen bestaan uit verschillende getallen of strings. Die data wordt van **elkaar gescheiden door een komma.**

**Een voorbeeld van een lijst:**
´´´
hoofdsteden_provincie = ['Brugge', 'Gent', 'Leuven']
´´´

**Voordelen van een lijst:**
Een lijst kan je bewaren in een variabele. Je kan er doorheen jouw algoritme data aan toevoegen uit een berekening of herhaling aan berekeningen. 
Je kan een lijst ook gebruiken om over te **itereren**, dit je zeggen dat je elk item uit de lijst kan halen, een bewerking uitvoeren, vervolgens het volgende item uit de lijst halen ... 


**Data toevoegen aan een bestaande lijst:** 
Wanneer we data willen toevoegen aan het einde van een bestaande lijst gebruiken we de **append-functie.**
De **syntax** van de **append-functie** gaat als volgt: 
´´´
# Hoe te lezen: 
# voeg toe. aan het einde deze lijst (dit item)
naam_lijst.append(item_dat_je_wil_toevoegen)

´´´

**Opgave:**

Bekijk volgende code: 

´´´
hoofdsteden_provincie = ['Brugge', 'Gent', 'Leuven']

´´´

Er ontbreken hier enkele Vlaamse provinciehoofdsteden, namelijk Hasselt en Antwerpen. (Brussel is technisch gezien de hoofdstad van een gewest)

* Vul het algoritme verder aan en voeg de ontbrekende hoofdsteden toe aan de bestaande lijst; 
* Gebruik hierbij de **append-functie**; 
* Print de resultaten naar het scherm in een volzin; 
* Een volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ...; 
* Bijvoorbeeld: 'De hoofdsteden van de Vlaamse provincies zijn: Brugge, Gent, Leuven ...'. 