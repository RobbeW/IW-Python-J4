Er bestaat een methode om manueel te controleren of een getal deelbaar is door 7. De methode werkt als volgt:

- Verdubbel het cijfer van de eenheden;
- Bereken het verschil van het getal zonder het cijfer van de eenheden en het vorig getal;
- Is dit verschil duidelijk deelbaar door 7, dan ben je klaar. Zo niet, herhaal.

## Opgave

Schrijf een programma dat een natuurlijk getal aan de gebruiker vraagt. Vervolgens voer je het bovenstaande algoritme uit, tot je een getal van 2 cijfers hebt. Je programma geeft elke stap van dit algoritme weer.

#### Voorbeelden
De invoer `3024` levert als uitvoer

```
1e stap: Het verschil van 302 en 8 is 294
2e stap: Het verschil van 29 en 8 is 21
```
Omdat 21 nu duidelijk deelbaar is door 7 kan je besluiten dat 3 024 ook deelbaar is door 7.

De invoer `153024` levert als uitvoer

```
1e stap: Het verschil van 15302 en 8 is 15294
2e stap: Het verschil van 1529 en 8 is 1521
3e stap: Het verschil van 152 en 2 is 150
4e stap: Het verschil van 15 en 0 is 15
```
Gezien 15 niet deelbaar is door 7 kan je besluiten dat 153 024 ook ondeelbaar is door 7.