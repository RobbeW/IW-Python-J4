Wetenschappers en ingenieurs controleren bijna nooit op gelijkheid, maar op **bijna gelijkheid**. Indien men bijvoorbeeld een kracht van 150 Newton wil bepalen dan zal dat in de praktijk nooit **exact** 150 Newton zijn. Maar bijvoorbeeld 150,1 Newton of 149,9 Newton. Afhankelijk van de toepassing kan dit even goed zijn.

## Opgave

Schrijf een functie `bijnagelijk(a, b, tolerantie)` die voor twee getallen `a` en `b` gaat bepalen of deze minder dan of evenveel als de `tolerantie` van elkaar verschillen. De `return`-waarde van deze functie is ofwel `True` ofwel `False`.

Vraag **vervolgens** twee kommagetallen aan de gebruiker en een tolerantie. Gebruik daarna de functie `bijnagelijk()` om na te gaan of deze getallen dicht genoeg van elkaar liggen. Afhankelijk van de waarde van deze functie wordt er een bepaalde zin op het scherm weergegeven.

#### Voorbeelden
Indien men als eerste getal `150.0` ingeeft en als tweede `150.1` met een tolerantie van `0.5`, dan liggen deze getallen dicht genoeg in elkaars buurt en verschijnt er:

```
150.0 en 150.1 zijn bijna aan elkaar gelijk.
```

Indien men als eerste getal `150.0` ingeeft en als tweede `150.1` met een tolerantie van `0.01`, dan liggen deze getallen **niet** dicht genoeg in elkaars buurt en verschijnt er:

```
150.0 en 150.1 verschillen teveel.
```