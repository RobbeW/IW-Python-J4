**Gegeven:**

Voor een onderzoek aan de universiteit is men geïnteresseerd in de dubbele familienamen in een bepaalde, relatief kleine, regio. Daarvoor hebben ze een lijst opgesteld met de familienamen van de inwoners van die kleine regio. 

<img src="https://images.pexels.com/photos/164686/pexels-photo-164686.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" width="50%"/>

**De Count-Functie**
Een **lijst** bevat ruim 200 namen. Teveel om zelf uit te zoeken welke namen meer dan één keer voorkomen. 
Via de **count-functie** kunnen we tellen hoeveel keer een **item** voorkomt in een lijst. 
De **syntaxis** van zo een **count-functie** is: 

```
naam_variabele = naam_lijst.count(wat_wil_je_tellen)

of 

aantal_keer = lijst_namen.count('Bram')
```

**Opgave:**
Je krijgt onderstaande begin van een algoritme. Bekijk de code grondig. 

```
lijst_namen=['Drake', 'Rodriguez', 'Estrada', 'Snow', 'Whitaker', 'Hull', 'Miranda', 'Evans', 'Gallagher', 'Wiley', 'Griffith', 'Brady', 'Yu', 'Hahn', 'Franco', 'Chandler', 'Stuart', 'Huang', 'Marks', 'Wiley', 'Harrell', 'Morrow', 'Sparks', 'Hebert', 'House', 'Luna', 'Russo', 'Hall', 'Vaughn', 'Fisher', 'Miller', 'Duncan', 'Lyons', 'Guzman', 'Ellis', 'Larson', 'Cruz', 'Avila', 'Rodgers', 'Andersen', 'Friedman', 'Edwards', 'Carter', 'Terrell', 'Castaneda', 'Ford', 'Palmer', 'Wilkinson', 'Norman', 'Holmes', 'Gillespie', 'Oneill', 'Mccullough', 'Hatfield', 'Roberson', 'Kramer', 'Wilcox', 'Howe', 'Frey', 'Crawford', 'Jacobs', 'Clay', 'Horn', 'Velez', 'Burton', 'Curtis', 'Morales', 'Choi', 'Terrell', 'Sandoval', 'Riddle', 'Wilkinson', 'Dickson', 'Leblanc', 'Sloan', 'Escobar', 'Moran', 'Hamilton', 'Reeves', 'Jenkins', 'Hardin', 'Jensen', 'Casey', 'Acevedo', 'Benitez', 'Rogers', 'Dunlap', 'Duran', 'Yu', 'Lamb', 'Freeman', 'Howe', 'Pennington', 'Watkins', 'Waters', 'Best', 'Le', 'Alexander', 'Harper', 'Giles', 'Levine', 'Davis', 'Dillon', 'Avila', 'Charles', 'Sandoval', 'Escobar', 'Pacheco', 'Bender', 'Fox', 'Brady', 'Riggs', 'Moran', 'Hood', 'Cherry', 'Myers', 'Mckinney', 'Carey', 'Richmond', 'Patel', 'Gay', 'Holder', 'Mckenzie', 'Good', 'Ryan', 'Solomon', 'Ruiz', 'Farmer', 'Terry', 'Lucero', 'Becker', 'Riddle', 'Boyer', 'Bean', 'Fuentes', 'Shea', 'Carrillo', 'Bridges', 'Lucas', 'Espinoza', 'Salinas', 'Mullins', 'Pratt', 'Todd', 'Foley', 'Vaughan', 'Jackson', 'Harrison', 'Schaefer', 'Murillo', 'Bryant', 'Riley', 'Mcconnell', 'Clements', 'Tanner', 'Bonilla', 'Donaldson', 'Leach', 'Cummings', 'Ali', 'Waters', 'Wells', 'Livingston', 'Schmitt', 'Reilly', 'Shepherd', 'Skinner', 'Hawkins', 'Charles', 'Perry', 'Paul', 'Hardin', 'Benton', 'Wilkins', 'Velez', 'Alvarez', 'Golden', 'Tanner', 'Pittman', 'Garcia', 'Keith', 'Nash', 'Frazier', 'Costa', 'Cain', 'Galloway', 'Newton', 'Costa', 'Galloway', 'Solomon', 'Daugherty', 'Villa', 'Stein', 'Freeman', 'Dunlap', 'Padilla', 'Collier', 'Salas', 'Castillo', 'McneilDrake']

for i in lijst_namen: 
    aantal = lijst_namen.count(i)

```

* Ga op zoek naar namen die méér dan één keer voorkomen; 
* Vul het algoritme verder aan; 
* Print te resultaten naar het scherm in een correcte volzin; 
* Een correcte volzin bevat een onderwerp, werkwoord, hoofdletters, leestekens ... 
* **Test** en **debug** voor je indient. 