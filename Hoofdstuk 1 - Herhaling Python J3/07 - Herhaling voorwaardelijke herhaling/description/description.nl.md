Een **voorwaardelijke herhaling** is een herhaling van acties die blijft lopen **zolang** aan de voorwaarde wordt voldaan. Dus zolang de uitkomst van onze voorwaarde `True` is, zullen de acties onder de herhaling herhaald worden. 

Een voorbeeld van zo'n herhaling: 
- Je bent pannenkoeken aan het bakken;
- Je laat die liggen totdat het deeg aan de bovenzijde niet meer lopend is;
  Met andere woorden: **zolang** het deeg lopend is, blijf je bakken; 
- Wanneer de toplaag niet meer lopend is, draai je deze om. 

## Syntax

Voor een voorwaardelijke herhaling gebruiken we volgende syntax: 

```python
while voorwaarde: 
    <acties>
```

Het vorige voorbeeld zou zich vertalen naar dit stukje *pseudocode*:

```python
while deeg != gestold: 
    bakken()
omdraaien() 
```

## Opgave

Schrijf een programma dat continu om **gehele** getallen vraagt, **totdat** het getal `-1` ingevoerd wordt.
Het programma geeft vervolgens het gemiddelde van alle ingevoerde getallen, afgerond op 2 cijfers na de komma.

#### Voorbeeld

Voor de achtereenvolgende invoer van `5`, `1`, `0`, `0`, `15` en `-1` verschijnt er:
```
Het gemiddelde van de getallen is 4.2
```