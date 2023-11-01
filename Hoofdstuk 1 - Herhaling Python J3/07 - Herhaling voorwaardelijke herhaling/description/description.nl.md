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

Door de klimaatopwarming komen hittegolven steeds vaker voor. Het KMI gebruikt de volgende definitie voor een hittegolf: 

{: .callout.callout-danger}
> Ten minste vijf dagen achtereen waarop de maximumtemperatuur 25,0°C of meer bedraagt (zogenaamde **zomerse dagen**); waarbij ten minste op drie dagen de maximumtemperatuur 30,0°C of meer bedraagt (zogenaamde **tropische dagen**).

Schrijf een programma dat de gebruiker telkens om de maximale dagtemperatuur vraagt. Het programma stopt nadat er **drie tropische dagen** werden ingevoerd en geeft nadien het totale aantal dagen en de hoogste temperatuur weer op het scherm.

#### Voorbeeld
Bij achtereenvolgende invoer van de volgende 7 temperaturen `27.6`, `29.1`, `31.1`, `28.0`, `30.0`, `25.1` en `30.5` verschijnt er:

```
Er werden 7 temperaturen ingevoerd.
De hoogste temperatuur was 31.1 °C.
```